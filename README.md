# KPA Backend API Assignment

Developed By: Maitri Shinde

Project Overview:
This project implements two backend APIs as part of the KPA assignment using FastAPI and PostgreSQL. The goal is to demonstrate backend development skills including API creation, database integration, and input validation.

How to Set Up the Project:

1. Prerequisites:
   - Python 3.8+
   - PostgreSQL installed and running
   - Database name: kpadb
   - Git (optional)

2. Installation Steps:
   - Clone the project folder
   - Open terminal and navigate to the project folder

   Create and activate virtual environment:
   - python -m venv venv
   - .\venv\Scripts\activate  (for Windows)
   - source venv/bin/activate (for macOS/Linux)

   Install dependencies:
   - pip install -r requirements.txt

   Set up environment variables:
   - Create a file named `.env` in the project root
   - Add:
     DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/kpadb

   Run the server:
   - uvicorn app.main:app --reload

   Access Swagger UI at:
   - http://127.0.0.1:8000/docs

Test User Credentials:
  - phone_number: 7760873976
  - password: to_share@123

Key Features Implemented:

1. POST /user/login
   - Accepts phone number and password via JSON
   - Authenticates the user against the PostgreSQL database

2. POST /upload
   - Accepts file upload via multipart form-data
   - Returns uploaded filename and type

3. Swagger UI Documentation
   - Auto-generated interface for testing APIs

4. PostgreSQL Database Integration
   - User data is fetched using SQLAlchemy ORM

Limitations and Assumptions:

- Passwords are stored as plain text (no encryption or hashing)
- No authentication tokens (JWT, OAuth) are used
- Uploaded files are not stored on disk
- Project is built for local testing only
- Signup or user registration API is not included

Thank You

