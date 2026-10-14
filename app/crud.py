
from app.database import database_connection, DATABASE_URL
from app.schemas import StudentCreate, StudentUpdate


PLACEHOLDER = "%s" if DATABASE_URL else "?"


def row_to_dict(row):
    return dict(row) if row is not None else None


def create_student(student: StudentCreate):
    data = student.model_dump(mode="json")

    with database_connection() as conn:
        if DATABASE_URL:
            row = conn.execute(
                """
                INSERT INTO students (
                    name, date_of_birth, email, phone,
                    course, address, enrollment_date
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    data["name"],
                    data["date_of_birth"],
                    data["email"],
                    data["phone"],
                    data["course"],
                    data["address"],
                    data["enrollment_date"],
                ),
            ).fetchone()

            return row_to_dict(row)

        cursor = conn.execute(
            """
            INSERT INTO students (
                name, date_of_birth, email, phone,
                course, address, enrollment_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["name"],
                data["date_of_birth"],
                data["email"],
                data["phone"],
                data["course"],
                data["address"],
                data["enrollment_date"],
            ),
        )

        row = conn.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (cursor.lastrowid,),
        ).fetchone()

        return row_to_dict(row)


def list_students(
    name=None,
    course=None,
    born_after=None,
    limit=20,
    offset=0,
):
    sql = "SELECT * FROM students WHERE 1=1"
    params = []

    if name:
        sql += f" AND name LIKE {PLACEHOLDER}"
        params.append(f"%{name}%")

    if course:
        sql += f" AND course LIKE {PLACEHOLDER}"
        params.append(f"%{course}%")

    if born_after:
        sql += f" AND date_of_birth > {PLACEHOLDER}"
        params.append(born_after.isoformat())

    sql += f" ORDER BY student_id LIMIT {PLACEHOLDER} OFFSET {PLACEHOLDER}"
    params.extend([limit, offset])

    with database_connection() as conn:
        rows = conn.execute(sql, params).fetchall()
        return [row_to_dict(row) for row in rows]


def get_student(student_id: int):
    with database_connection() as conn:
        row = conn.execute(
            f"SELECT * FROM students WHERE student_id = {PLACEHOLDER}",
            (student_id,),
        ).fetchone()

        return row_to_dict(row)


def update_student(student_id: int, student: StudentUpdate):
    data = student.model_dump(mode="json")

    with database_connection() as conn:
        cursor = conn.execute(
            f"""
            UPDATE students SET
                name = {PLACEHOLDER},
                date_of_birth = {PLACEHOLDER},
                email = {PLACEHOLDER},
                phone = {PLACEHOLDER},
                course = {PLACEHOLDER},
                address = {PLACEHOLDER},
                enrollment_date = {PLACEHOLDER},
                updated_at = CURRENT_TIMESTAMP
            WHERE student_id = {PLACEHOLDER}
            """,
            (
                data["name"],
                data["date_of_birth"],
                data["email"],
                data["phone"],
                data["course"],
                data["address"],
                data["enrollment_date"],
                student_id,
            ),
        )

        if cursor.rowcount == 0:
            return None

        row = conn.execute(
            f"SELECT * FROM students WHERE student_id = {PLACEHOLDER}",
            (student_id,),
        ).fetchone()

        return row_to_dict(row)


def delete_student(student_id: int):
    with database_connection() as conn:
        cursor = conn.execute(
            f"DELETE FROM students WHERE student_id = {PLACEHOLDER}",
            (student_id,),
        )

        return cursor.rowcount > 0
