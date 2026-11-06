# Production-Style Inventory Management REST API

## Project Overview
this project is a Python Flask-based Inventory Management REST API that allows users to manage products through CRUD operations.

It is developed as a hands-on Cloud and DevOps portfolio project to practice application development, automated testing, Git version control, and CI/CD workflows.

## Technologies Used
- Python
- Flask
- REST API
- Pytest
- Git
- GitHub
- Linux (Ubuntu)

## Project Structure

```text
production-devops-project/
├── app/
│   └── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home page |
| GET | `/health` | Health check |
| POST | `/products` | Add a product |
| GET | `/products` | Get all products |
| GET | `/products/<id>` | Get a product by ID |
| PUT | `/products/<id>` | Update a product |
| DELETE | `/products/<id>` | Delete a product |

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd production-devops-inventory-management
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app/app.py
```

Application URL: `http://localhost:5000`

Health check: `http://localhost:5000/health`

## Automated Testing

Run automated tests using:

```bash
python -m pytest
```

Current test coverage includes:
- Home endpoint
- Health endpoint
- Add product endpoint
- Get all products endpoint

## Current Project Status

- Flask REST API developed.
- Product CRUD endpoints implemented.
- Automated tests created using Pytest.
- Dependencies documented in requirements.txt.
- Git repository initialized.
- GitHub repository configured.

## Future Improvements

- Jenkins CI/CD pipeline
- Docker containerization
- Kubernetes deployment
- Cloud deployment using AWS and Azure
- Persistent database integration
- Monitoring and logging

## Author

Cloud & DevOps Engineering Learner

This project is continuously being improved as part of practical Cloud and DevOps learning.
