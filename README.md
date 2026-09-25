# Doctor–Patient Management API

A production-ready backend application built using **FastAPI** for managing doctors, patients, authentication, authorization, and doctor–patient assignments.

---

## 1. Project Overview

The Doctor–Patient Management API provides a secure backend system with:

* JWT-based authentication
* Role-based authorization
* Admin and Doctor roles
* Doctor management
* Patient management
* Doctor–patient assignment
* Input validation
* SQLite database persistence
* Soft deletion of doctors
* Swagger/OpenAPI documentation
* Environment-based configuration

The application follows a modular architecture with separate routers, models, schemas, services, and authentication modules.

---

## 2. Technology Stack

| Technology                        | Purpose                     |
| --------------------------------- | --------------------------- |
| Python 3.9+                       | Programming language        |
| FastAPI                           | Backend web framework       |
| Pydantic                          | Request/response validation |
| SQLAlchemy                        | ORM/database interaction    |
| SQLite                            | Database                    |
| JWT                               | Authentication              |
| Uvicorn                           | ASGI server                 |
| Passlib/Bcrypt                    | Password hashing            |
| python-dotenv / Pydantic Settings | Environment configuration   |
| Swagger/OpenAPI                   | API documentation           |

---

## 3. Project Structure

```text
doctor_patient_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── auth.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── doctors.py
│   │   └── patients.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── doctor_service.py
│       └── patient_service.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── doctor_patient.db
```

### Module Responsibilities

**main.py**

* Creates the FastAPI application
* Registers routers
* Initializes database tables

**database.py**

* Database configuration
* SQLAlchemy engine
* Database session management

**models.py**

* SQLAlchemy database models
* User, Doctor, Patient and relationships

**schemas.py**

* Pydantic request and response models
* Input validation

**auth/**

* Password hashing
* JWT creation and validation
* Authentication and role authorization

**routers/**

* API endpoints
* Request handling
* HTTP responses

**services/**

* Business logic
* Database CRUD operations

---

## 4. Installation

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd doctor_patient_api
```

---

### Step 2: Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Environment Configuration

Create a `.env` file in the project root.

```env
DATABASE_URL=sqlite:///./doctor_patient.db
SECRET_KEY=change-this-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## 6. Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

---

## 7. API Documentation

FastAPI automatically provides Swagger documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Swagger can be used to test all API endpoints.


# 8. User Roles

The application supports two roles.

## Admin

Admin users can:

* Create doctors
* View doctors
* Update doctors
* Soft-delete doctors
* Create patients
* View patients
* Assign patients to doctors

## Doctor

Doctor users can:

* Authenticate using JWT
* View their assigned patients
* Access only the patients assigned to them

Doctors cannot manage other doctors or access another doctor's patients.

---

# 10. Authentication APIs

## Register

```http
POST /auth/register
```

Example request:

```json
{
  "username": "admin",
  "email": "admin@example.com",
  "password": "Admin@123",
  "role": "admin"
}
```

Example Doctor registration:

```json
{
  "username": "doctor1",
  "email": "doctor1@example.com",
  "password": "Doctor@123",
  "role": "doctor"
}
```

---

## Login

```http
POST /auth/login
```

Example request:

```json
{
  "username": "admin",
  "password": "Admin@123"
}
```

Example response:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

Copy the access token and use it in Swagger's **Authorize** button.

---

# 11. Doctor Management APIs

## Create Doctor

```http
POST /doctors
```

**Authorization:** Admin only.

Example:

```json
{
  "name": "Dr. Ravi Kumar",
  "specialization": "Cardiology",
  "email": "ravi@example.com",
  "is_active": true
}
```

---

## List Doctors

```http
GET /doctors
```

Returns the list of doctors.

---

## Get Doctor

```http
GET /doctors/{doctor_id}
```

Example:

```text
GET /doctors/1
```

---

## Update Doctor

```http
PUT /doctors/{doctor_id}
```

Example:

```json
{
  "name": "Dr. Ravi Kumar",
  "specialization": "Neurology",
  "email": "ravi@example.com",
  "is_active": true
}
```

---

## Delete Doctor

```http
DELETE /doctors/{doctor_id}
```

The application uses **soft deletion** instead of permanently deleting the doctor.

The doctor is marked as:

```json
{
  "is_active": false
}
```

---

# 12. Patient Management APIs

## Create Patient

```http
POST /patients
```

Example:

```json
{
  "name": "prasanth",
  "age": 25,
  "phone": "9876543210"
}
```

---

## List Patients

```http
GET /patients
```

Returns the available patients.

---

## Get Patient

```http
GET /patients/{patient_id}
```

Example:

```text
GET /patients/1
```

---

# 13. Doctor–Patient Assignment

A doctor can have multiple patients.

## Assign Patient

```http
POST /doctors/{doctor_id}/patients/{patient_id}
```

Example:

```text
POST /doctors/1/patients/1
```

This assigns patient `1` to doctor `1`.

---

## Get Doctor's Patients

```http
GET /doctors/{doctor_id}/patients
```

Example:

```text
GET /doctors/1/patients
```

The response contains only patients assigned to that doctor.

Doctors are restricted from viewing patients assigned to other doctors.

---

# 14. Validation

The API implements validation using Pydantic.

## Email

Email addresses must be valid and unique.

Example:

```text
doctor@example.com
```

Invalid:

```text
doctor-example
```

---

## Age

Age must be greater than zero.

Valid:

```json
{
  "age": 25
}
```

Invalid:

```json
{
  "age": 0
}
```

---

## Phone

Phone numbers must contain between 10 and 15 digits.

Valid:

```text
9876543210
```

Invalid:

```text
12345
```

---

# 15. Error Handling

The application uses FastAPI's `HTTPException` for API errors.

Examples include:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
422 Validation Error
```

Example:

```json
{
  "detail": "Doctor not found"
}
```

---

# 16. Database

SQLite is used as the database for this assignment.

Database:

```text
doctor_patient.db
```

Main entities:

```text
Users
Doctors
Patients
Doctor_Patient
```

Relationship:

```text
Doctor
   |
   |--- Patient
   |
   |--- Patient
   |
   |--- Patient
```

A many-to-many relationship is used so the database can support multiple patient assignments.

---


# 17. Testing

The APIs can be tested using:

* FastAPI Swagger UI
* Postman
* cURL

Swagger:

```text
http://127.0.0.1:8000/docs
```

Recommended testing sequence:

```text
1. Register Admin
2. Login Admin
3. Authorize JWT
4. Create Doctor
5. Create Patient
6. Assign Patient
7. Get Doctor's Patients
8. Register Doctor
9. Login Doctor
10. Verify Doctor can access assigned patients
11. Verify Doctor cannot access another doctor's patients
12. Verify Admin-only endpoints return 403 for Doctor
13. Test invalid email
14. Test invalid age
15. Test invalid phone
16. Test duplicate email
17. Test non-existing Doctor/Patient
```

---

# 18. Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Generate/update the file using:

```bash
pip freeze > requirements.txt
```


