# CodeLeap API Test

This project is a test case using Django and Django REST Framework (DRF). The API enables users to create, read, update, and delete career entries.

### Online URL for CURL
```url
https://mrcadu7.pythonanywhere.com/careers/
```

## Running Locally

### 1. Install Dependencies and Environment Variables Configuration

Before starting the project, it's necessary to configure some essential environment variables for the application to function properly. Follow the steps below to set them up:

Create a file named .env at the root of the project.
Open the .env file you created and add the following variables, replacing VALUE with the appropriate values for your environment:

```env
SECRET_KEY=VALUE
DEBUG=VALUE
```

## Required Variables

- SECRET_KEY: Secret key for application security.

- DEBUG: Sets the debug mode (True for development, False for production).


### .env.example File
An .env.example file is included in the repository as a template. You can copy it to create your own .env file, remembering to replace the example values with the real ones.

## This project requires the following dependencies:

- Python 3.12
- Django 5.0.2
- Django Rest Framework 3.14.0
- Docker 24.0.7 (for running the application with Docker)

You can install the Python dependencies with pip:

```bash
pip install -r requirements.txt
```

Please ensure that you have installed the correct versions of these dependencies before running the application.

### 2. Start the Application

After installing the dependencies, you can start the application by running the following command:

```bash
python manage.py runserver
```

## Running with Docker

### This project has been Dockerized to make it easy to run in any environment. To run the application with Docker, follow this simple step:


- Build the Docker image from the Dockerfile:


```bash
docker-compose up
```

## Now, the application should be running at http://localhost:8000


# Data Structure

### Each career is represented by an object with the following structure:

```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
```

## API Operations

This API facilitates career management. It supports operations for creating, reading, updating, and deleting career entries.

### The API supports the following operations:


- **POST** to `https://localhost:8000/careers/` to create a new career. The request body should be a JSON object with the fields `username`, `title`, and `content`.

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"username": "user1", "title": "title1", "content": "content1"}' https://localhost:8000/careers/
    ```
  

- **GET** to `https://localhost:8000/careers/` to retrieve the list of careers.

    ```bash
    curl https://localhost:8000/careers/
    ```
  

- **PATCH** to `https://localhost:8000/careers/{OBJECT_ID}/` to update an existing career. The request body should be a JSON object with the fields `title` and `content`. The fields `id`, `username`, and `created_datetime` cannot be changed.

    ```bash
    curl -X PATCH -H "Content-Type: application/json" -d '{"title": "Updated Title", "content": "Updated Content"}' https://localhost:8000/careers/{OBJECT_ID}/
    ```
  

- **DELETE** to `https://localhost:8000/careers/{OBJECT_ID}/` to delete a career.

    ```bash
    curl -X DELETE https://localhost:8000/careers/{OBJECT_ID}/
    ```


## Tests

The project includes a comprehensive suite of tests to ensure the API functions correctly. These tests cover CRUD operations as well as custom validations.

### Running the Tests

To run the tests, navigate to the root directory of the Django project and execute the following command:

```bash
python manage.py test
```

This command will execute all defined tests in the Django project and display the results in the terminal.

