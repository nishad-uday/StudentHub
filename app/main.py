
from contextlib import asynccontextmanager
from datetime import date

from fastapi import FastAPI, HTTPException, Query, Response, status

from app import crud
from app.config import APP_NAME, APP_VERSION
from app.database import init_db
from app.schemas import StudentCreate, StudentUpdate, StudentResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Lightweight Student Database CRUD API",
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {
        "message": "StudentHub API is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student: StudentCreate):
    return crud.create_student(student)


@app.get("/students", response_model=list[StudentResponse])
def get_students(
    name: str | None = Query(default=None, max_length=100),
    course: str | None = Query(default=None, max_length=100),
    born_after: date | None = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return crud.list_students(
        name=name,
        course=course,
        born_after=born_after,
        limit=limit,
        offset=offset,
    )


@app.get(
    "/students/{student_id}",
    response_model=StudentResponse,
)
def get_student(student_id: int):
    student = crud.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student


@app.put(
    "/students/{student_id}",
    response_model=StudentResponse,
)
def update_student(student_id: int, student: StudentUpdate):
    updated = crud.update_student(student_id, student)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return updated


@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(student_id: int):
    deleted = crud.delete_student(student_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
