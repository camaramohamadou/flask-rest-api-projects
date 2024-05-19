
- **`data/products.json`**: JSON file to store product data.
- **`requirements.txt`**: List of dependencies.
- **`src/app.py`**: Main Flask application file.
- **`src/models.py`**: Functions to handle data persistence.
- **`src/routes.py`**: API routes for managing products.

## Setup 

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- Docker (for containerization)
- Google Cloud SDK (for deploying to Google Cloud Run)

### Running the Server Locally and with Docker

#### Install Dependencies

1. **Create and Activate a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. **Install Dependencies:**:

   ```bash
   pip install -r requirements.txt

3. **Run the Flask Application:**:

   ```bash
   python -m src.app

