
- **`Dockerfile`**: Defines the Docker image for the Flask application.
- **`README.md`**: Documentation for the project.
- **`requirements.txt`**: List of dependencies.
- **`request.py`**: Client script to interact with the Flask API using the `requests` library.
- **`src/server.py`**: Main Flask application file.
- **`src/customers.json`**: JSON file to store customer data.
- **`tests/test_server.py`**: Unit tests for the Flask application.

## Server and Client Architecture

### Server

The server is built using Flask and provides the following API endpoints:

- `GET /api/customers`: Retrieve a list of all customers.
- `GET /api/customers/<id>`: Retrieve details of a specific customer by ID.
- `POST /api/customers`: Add a new customer.
- `PUT /api/customers/<id>`: Update details of an existing customer by ID.
- `DELETE /api/customers/<id>`: Delete a customer by ID.

### Client

The client script (`request.py`) uses the `requests` library to interact with the Flask API. It demonstrates how to perform CRUD operations on the customer data.

## Setup

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- Docker (for containerization)
- Google Cloud SDK (for deploying to Google Cloud Run)

### Clone the Repository

```bash
git clone https://github.com/camaramohamadou/flask-rest-api-projects.git
cd flask-rest-api-projects/customer-management-api
