
# Job Application Tracker

## Project Description

Job Application Tracker is a backend application built with Python, Flask, SQLAlchemy, and PostgreSQL.

The project is designed to manage job applications and track their statuses. It uses a relational database to organize information about users, profiles, companies, jobs, applications, and skills.

The application provides a REST API for creating, viewing, updating, and deleting job applications.

This project was originally developed during the SQL with Python course and is being extended as part of the Modern Software Engineering with DevOps course at Nucamp.

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Docker
- REST API
- SQL

## Database Design

The database contains seven tables:

- **users** — stores user information.
- **profiles** — stores additional user profile information.
- **companies** — stores company information.
- **jobs** — stores job postings and their associated companies.
- **applications** — connects users to jobs and tracks application statuses.
- **skills** — stores skill names.
- **job_skills** — connects jobs and skills through a many-to-many relationship.

The database uses primary keys and foreign keys to maintain relationships between tables.

## API Reference

### Existing Endpoints

| Method | Endpoint | Description | Parameters |
|---|---|---|---|
| GET | `/applications` | Retrieve all applications | None |
| POST | `/applications` | Create a new application | JSON body: `user_id`, `job_id`, `status` |
| PUT | `/applications/{application_id}` | Update an application's status | URL: `application_id`; JSON body: `status` |
| DELETE | `/applications/{application_id}` | Delete an application | URL: `application_id` |

### Planned Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/applications/{application_id}` | Retrieve a single application |
| GET | `/applications?status=Applied` | Filter applications by status |
| GET | `/companies` | Retrieve companies |
| GET | `/jobs` | Retrieve job postings |

### Example POST Request

```json
{
  "user_id": 1,
  "job_id": 1,
  "status": "Applied"
}
```

## Database Performance Optimization

A B-tree index was created on the `status` column of the `applications` table.

```sql
CREATE INDEX IF NOT EXISTS ix_applications_status
ON applications (status);
```

The index was verified in PostgreSQL using the `pg_indexes` system view.

This index can improve the performance of queries that filter applications by status, particularly as the table grows.

## Project Retrospective

### How did the project design evolve?

The project started with a relational database design for managing job applications. The database structure was organized around users, profiles, companies, jobs, applications, and skills.

The application was then connected to Flask using SQLAlchemy, and REST API endpoints were implemented to support basic CRUD operations.

During the performance optimization stage, a B-tree index was added to the application status column.

### Did you use an ORM or raw SQL? Why?

I used SQLAlchemy as an Object-Relational Mapper (ORM) to define database models and perform CRUD operations.

SQLAlchemy made it easier to work with PostgreSQL using Python objects and helped keep the application code organized.

I also used SQL directly to create and verify the database index.

### What would you improve in the future?

Future improvements could include:

- User authentication and authorization.
- Filtering applications by status.
- Search and sorting functionality.
- Better validation and error handling.
- Additional API endpoints for companies, jobs, and skills.
- A frontend dashboard to visualize application progress.
- Automated API tests.

## DevOps Progress - Week 2

This project builds on the Job Application Tracker developed during the SQL with Python course.

During Week 2, I started preparing the existing Flask application for containerization using Docker.

### Work Completed

- Reused the existing Flask REST API project.
- Created a `requirements.txt` file for Python dependencies.
- Created an initial `Dockerfile` using Python 3.12.
- Updated the Flask database configuration to support environment variables.
- Added a `.gitignore` file.
- Updated the project documentation for the DevOps course.
- Started preparing the project for containerized deployment.

### Docker Configuration

The initial Dockerfile uses a lightweight Python 3.12 image.

It sets up the application directory, installs Python dependencies, and copies the project files into the Docker image.

The Docker setup is currently in development. The application startup command and PostgreSQL container configuration still need to be completed and tested.

### Next Steps

- Configure Docker Compose for Flask and PostgreSQL.
- Test the application in Docker containers.
- Implement additional API endpoints.
- Add filtering and search functionality.
- Improve API validation and error handling.
- Add automated tests and CI/CD using GitHub Actions.
- Deploy the application to the cloud.

## Conclusion

This project demonstrates relational database design, PostgreSQL integration, Flask REST API development, CRUD operations, and database indexing.

The current DevOps phase focuses on Docker containerization, deployment preparation, and future automation.

The goal is to develop the application into a more complete job application management system.
