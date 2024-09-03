# Todo-app-Fastapi

## Project Overview

A To-do application to learn how to use FastAPI with SQLAlchemy and PostgreSQL.

## Installation

### Prerequisites

- Python 3.12.5

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

# Activate virtual environment
source venv/bin/activate

# Install depdendency packages
pip install -r requirements.txt
```

#### 3. Configure `.env` file by creating a copy from `.env.sample`

#### 4. Setup a postgres 

#### 5. Database migrations
 At `app` directory, run `alembic` migration command. Please make sure your postgres DB is ready and accessible. In case you want to use `SQLite` instead, please be sure to configure the `env.py` file in `alembic` folder to support `batch execution` since `SQLite` does not support `ALTER` command, which is needed to configure the foreign key and establish the indexes.
```bash
# Migrate to latest revison
alembic upgrade head

# Dowgragde to specific revision
alembic downgrade <revision_number>

# Downgrade to base (revert all revisions)
alembic downgrade base

# Create new revision
alembic revision -m <comment>
```   

## Usage
- Run `uvicorn` web server from `app` directory (`reload` mode is for development purposes):
    ```bash
    uvicorn main:app --reload
    ```
- Open your browser and go to: http://127.0.0.1:8000
- To access the FastAPI documentation, visit: http://127.0.0.1:8000/docs