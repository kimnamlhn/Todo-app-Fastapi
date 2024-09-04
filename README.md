# Todo-app-Fastapi

## Project Overview

A To-do application to learn how to use FastAPI with SQLAlchemy and PostgreSQL.

## API Documentation 
Below are the endpoints in the project. For more details, see the [Demo video](https://www.youtube.com/watch?v=w43f_5inPYk)
- Company
   - Get all companies
   ```http
   GET /company
   ```
   - Create a company
   ```http
   POST /company
   ```
   - Get a company by id
   ```http
   GET /company/company_id
   ```
  - Update a company
   ```http
   PUT /company/company_id
   ```
   - Delete a company
   ```http
   DELETE /company/company_id
   ```
- User
   - Get all users
   ```http
   GET /users
   ```
   
- Task
   - Get all task
   ```http
   GET /tasks
   ```
   
 - Healthcheck
   ```http
   GET /
   ```
 - Auth
     - Login for access token
     ```http
     POST /auth/token
     ```
## Installation

### Prerequisites

- Python 3.12.5
- PostgreSQL
- pgAdmin 4

### Steps

#### 1. Clone the repository:
```bash
git clone https://github.com/kimnamlhn/Todo-app-Fastapi.git
```
#### 2. Create a virtual environment using `virtualenv` module in python.
```bash

# Install module (globally)
pip install virtualenv

# Generate virtual environment
virtualenv --python=<your-python-runtime-version> venv

# Install depdendency packages
pip install -r requirements.txt
```

#### 3. Configure `.env` file by creating a copy from `.env.sample`
 - Example:
![image](https://github.com/user-attachments/assets/a7dbdcc4-2613-48e4-a7be-dafa4a36f148)

#### 4. Setup a PostgresSQL 
- Install PostgreSQL and pgAdmin
- Create a new database and add the necessary information (e.g., host, username, password) to the .env file

#### 5. Database migrations
 At `app` directory, run `alembic` migration command. 
```bash
alembic upgrade head
```   

## Usage
- Run `uvicorn` web server from `app` directory (`reload` mode is for development purposes):
    ```bash
    uvicorn main:app --reload
    ```
- Open your browser and go to: http://127.0.0.1:8000
- To access the FastAPI documentation, visit: http://127.0.0.1:8000/docs
