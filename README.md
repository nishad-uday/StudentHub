# StudentHub API

A student database CRUD REST API built using **Python, FastAPI, SQLite, and PostgreSQL**. The project includes input validation, filtering, pagination, automated tests, Docker support, and cloud deployment.

## Live Demo

- **Live API:** https://studenthub-api-gaq8.onrender.com
- **Interactive API Documentation:** https://studenthub-api-gaq8.onrender.com/docs
- **Health Check:** https://studenthub-api-gaq8.onrender.com/health
- **GitHub Repository:** https://github.com/nishad-uday/StudentHub

> Note: The API is hosted on Render's Free plan. The first request after inactivity may take some time while the service starts.

## Overview

StudentHub API provides REST endpoints to create, retrieve, update, and delete student records. It supports filtering, pagination, input validation, and appropriate error handling.

The application uses SQLite for local development and Neon PostgreSQL for the deployed environment through the `DATABASE_URL` environment variable.

## Features

- Create student records
- Retrieve all students or a student by ID
- Update existing student information
- Delete student records
- Filter students by name, course, and date of birth
- Pagination using `limit` and `offset`
- Input validation with Pydantic
- Appropriate HTTP status codes and error responses
- Interactive Swagger UI documentation
- Automated tests using pytest
- Docker support
- Cloud deployment on Render
- PostgreSQL database hosted by Neon

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| SQLite | Local development database |
| PostgreSQL | Production database |
| Neon | Hosted PostgreSQL database |
| Pydantic | Data validation and schemas |
| Uvicorn | ASGI server |
| pytest | Automated testing |
| Docker | Containerization |
| Render | API hosting |

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
├── render.yaml
└── requirements.txt
```

Local files such as `students.db`, virtual environments, and cache directories may be generated when running the project. They should not be committed to GitHub.

## Requirements

- Python 3.12 or a compatible Python version
- pip
- Git
- Docker Desktop (optional)

## Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/nishad-uday/StudentHub.git
cd StudentHub
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python -m uvicorn app.main:app --reload
```

Open these URLs in your browser:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

By default, the local application uses SQLite. Set `DATABASE_PATH` if you want to specify a different SQLite database location.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| POST | `/students` | Create a student |
| GET | `/students` | List, filter, and paginate students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

### Example: Create a Student

**Request:** `POST /students`

```json
{
  "name": "Aman Verma",
  "date_of_birth": "2003-05-15",
  "email": "aman.verma.demo@example.com",
  "phone": "9876543210",
  "course": "B.Tech CSE",
  "address": "Raipur, Chhattisgarh",
  "enrollment_date": "2024-08-01"
}
```

A successful request returns `201 Created` with the created student record.

### Filtering and Pagination

The `GET /students` endpoint supports:

- `name` — filter by student name
- `course` — filter by course
- `born_after` — filter by date of birth
- `limit` — maximum number of records to return
- `offset` — number of records to skip

Example:

```text
GET /students?name=Aman&limit=20&offset=0
```

Use the interactive Swagger UI at `/docs` to explore and test all endpoints.

## Database Configuration

The application supports two database modes:

- **Local development:** SQLite database, using `DATABASE_PATH` or the default `students.db` path.
- **Deployment:** Neon PostgreSQL, configured through the `DATABASE_URL` environment variable.

Set `DATABASE_URL` in your hosting provider's environment settings. Do not commit database passwords, connection strings, or other secrets to GitHub.

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

### 3. Open the documentation

Visit http://127.0.0.1:8000/docs.

The named Docker volume is intended to persist the local SQLite database when the container is configured to use `/data/students.db`.

## Run Automated Tests

Activate your virtual environment and run:

```powershell
python -m pytest -v
```

The four tests that passed in the last recorded local test run were:

- `test_crud_flow`
- `test_invalid_student`
- `test_missing_student`
- `test_filter_and_pagination`

## Deployment

The API is deployed on Render and uses Neon PostgreSQL for hosted data storage.

- Live API: https://studenthub-api-gaq8.onrender.com
- API documentation: https://studenthub-api-gaq8.onrender.com/docs
- Health endpoint: https://studenthub-api-gaq8.onrender.com/health

The deployed CRUD operations were manually tested, including creating, listing, updating, and deleting student records.

## Future Improvements

- Add authentication and authorization
- Expand automated test coverage
- Build a web-based frontend
- Add database migrations
- Explore an optional AI-powered extension

## Author

Developed as a student project to practice REST API development, database operations, data validation, automated testing, containerization, and cloud deployment.
