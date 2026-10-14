# StudentHub API

A lightweight Student Database CRUD REST API built using **Python, FastAPI, and SQLite**, with Docker support and automated tests.

## Overview

StudentHub API provides REST endpoints to create, retrieve, update, and delete student records. It also supports filtering, pagination, input validation, and handling missing student records.

## Features

- Create new student records
- Retrieve all students or a student by ID
- Update existing student information
- Delete student records
- Filter students by name, course, and date of birth
- Pagination using `limit` and `offset`
- Input validation and appropriate HTTP error responses
- SQLite database storage
- Interactive API documentation using Swagger UI
- Automated testing with pytest
- Docker support with persistent database storage

## Tech Stack

- **Language:** Python
- **API Framework:** FastAPI
- **Database:** SQLite
- **Server:** Uvicorn
- **Testing:** pytest, FastAPI TestClient
- **Containerization:** Docker

## Project Structure

```text
StudentHub/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   └── schemas.py
├── tests/
│   └── test_api.py
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── students.db
```

*Note: `students.db`, `venv/`, and cache directories may be generated locally. Do not commit local database files, virtual environments, or caches to GitHub.*

## Requirements

- Python 3.12 or compatible Python version
- pip
- Docker Desktop (optional, for containerized execution)

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd StudentHub
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

- API base URL: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| POST | `/students` | Create a student |
| GET | `/students` | List and filter students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

### Example: Create a Student

**Request:** `POST /students`

```json
{
  "name": "Aman Verma",
  "date_of_birth": "2003-08-20",
  "email": "aman.verma@example.com",
  "phone": "9876501234"
}
```

A successful request returns `201 Created` with the student record.

### Filtering and Pagination

The `GET /students` endpoint supports these query parameters:

- `name` — filter by student name
- `course` — filter by course
- `born_after` — filter by date of birth
- `limit` — number of records to return
- `offset` — number of records to skip

Example:

```text
GET /students?name=Aman&limit=20&offset=0
```

Use `/docs` to explore and test all endpoints interactively.

## Run with Docker

Make sure Docker Desktop is running.

### 1. Build the image

```powershell
docker build -t studenthub-api .
```

### 2. Start the container

```powershell
docker run --rm -p 8000:8000 -v studenthub-data:/data studenthub-api
```

### 3. Open the API documentation

Visit `http://127.0.0.1:8000/docs`.

The named Docker volume `studenthub-data` is intended to persist the SQLite database at `/data/students.db`. Keep the `DATABASE_PATH` configuration pointed to that location when running with this volume.

## Run Automated Tests

Activate your virtual environment, then run:

```powershell
python -m pytest -v
```

The project has been tested locally with these four tests:

- `test_crud_flow`
- `test_invalid_student`
- `test_missing_student`
- `test_filter_and_pagination`

All four passed in the last recorded test run.

## Configuration

The database path can be configured using the `DATABASE_PATH` environment variable. If it is not provided, the application uses `students.db` in the project root.

## Future Improvements

- Add authentication and authorization
- Add more comprehensive API tests
- Add a web-based frontend
- Add deployment configuration
- Explore an optional AI-powered extension

## License

Add a license appropriate for your project before publishing it publicly.

## Author

Developed as a student project for learning REST API development, database operations, testing, and containerization.
