# Setting up Flask App with PostgreSQL Database

## Introduction

This README file provides instructions on how to set up a Flask application with a PostgreSQL database using Docker containers.
This setup includes creating a Docker network for communication between containers, a Docker volume for persisting PostgreSQL data,
cloning the project from GitHub, and creating a virtual environment (venv) using a requirements file.

## Prerequisites

- Docker installed on your machine.
- Git installed on your machine.
- Python installed on your machine.

## Setup Instructions

1. **Clone the Project from GitHub:**

```bash
git clone https://github.com/haimgoldfisher/flask-docker-postgres.git
```

2. **Create a Virtual Environment and Install Dependencies:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

1. **Create Docker Network and Volume:**

```bash
docker network create flask-gres-net
docker volume create postgres-vol
```

3. **Run PostgreSQL Container:**
   
```bash
docker run -e POSTGRES_DB=postgresdb -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin --name my-postgres -v postgres-vol:/var/lib/postgresql/ --network flask-gres-net -p 5432:5432 postgres
```

4. **Enter PostgreSQL Container and Create Table:**

```bash
docker exec -it my-postgres /bin/bash
psql -U admin -d postgresdb
```

5. **Inside the PostgreSQL container:**

```sql
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
```
6. **Build Flask App Image and Run Container:**

```bash
docker build -t my-app:1.1 .
docker run -p 5555:5555 --network flask-gres-net my-app:1.1
```

## Test Flask App Functionality:

Send some requests to check the app functionality and communication with PostgreSQL.

- **Add a user:**

```bash
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "haimon"}' http://127.0.0.1:5555/users
```

You can also add a user using 'Postman' App with the same params.

- **Get all users:**

```bash
curl -i -X GET http://127.0.0.1:5555/users
```




