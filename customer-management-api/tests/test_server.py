import pytest
import json
import os
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from server import server, DATA_FILE

@pytest.fixture
def client():
    server.config['TESTING'] = True
    server.config['DATA_FILE'] = DATA_FILE + ".test"
    client = server.test_client()

    # Set up a temporary file for testing
    with open(server.config['DATA_FILE'], 'w') as f:
        json.dump({
            "1": {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
            "2": {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 25},
            "3": {"name": "Emily Johnson", "email": "emily.johnson@example.com", "age": 35}
        }, f)

    yield client

    # Clean up the temporary file after tests
    os.remove(server.config['DATA_FILE'])

def test_get_all_customers(client):
    response = client.get('/api/customers')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    expected_customers = {
        "1": {"name": "John Doe", "email": "john.doe@example.com", "age": 30},
        "2": {"name": "Jane Smith", "email": "jane.smith@example.com", "age": 25},
        "3": {"name": "Emily Johnson", "email": "emily.johnson@example.com", "age": 35}
    }
    assert data == expected_customers

def test_get_single_customer(client):
    response = client.get('/api/customers/1')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    expected_customer = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
    assert data == expected_customer

def test_add_customer(client):
    new_customer = {"name": "Alice", "email": "alice@example.com", "age": 28}
    response = client.post('/api/customers', data=json.dumps(new_customer), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.get_data(as_text=True))
    assert data['customer']['name'] == 'Alice'

def test_update_customer(client):
    updated_customer = {"name": "John Doe", "email": "john.doe@newdomain.com", "age": 31}
    response = client.put('/api/customers/1', data=json.dumps(updated_customer), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data['customer'] == updated_customer

def test_delete_customer(client):
    response = client.delete('/api/customers/1')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert data['message'] == 'Customer deleted'
    response = client.get('/api/customers/1')
    assert response.status_code == 404
