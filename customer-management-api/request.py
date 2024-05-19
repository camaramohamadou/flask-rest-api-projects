import requests
import json

BASE_URL = 'http://localhost:5000/api/customers'

def get_all_customers():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("All Customers:")
        print(json.dumps(response.json(), indent=4))
    else:
        print("Error:", response.status_code)

def get_customer(customer_id):
    response = requests.get(f"{BASE_URL}/{customer_id}")
    if response.status_code == 200:
        print(f"Customer {customer_id}:")
        print(json.dumps(response.json(), indent=4))
    else:
        print("Error:", response.status_code)

def add_customer(name, email, age):
    new_customer = {"name": name, "email": email, "age": age}
    response = requests.post(BASE_URL, json=new_customer)
    if response.status_code == 201:
        print("Added Customer:")
        print(json.dumps(response.json(), indent=4))
    else:
        print("Error:", response.status_code)

def update_customer(customer_id, name, email, age):
    updated_customer = {"name": name, "email": email, "age": age}
    response = requests.put(f"{BASE_URL}/{customer_id}", json=updated_customer)
    if response.status_code == 200:
        print(f"Updated Customer {customer_id}:")
        print(json.dumps(response.json(), indent=4))
    else:
        print("Error:", response.status_code)

def delete_customer(customer_id):
    response = requests.delete(f"{BASE_URL}/{customer_id}")
    if response.status_code == 200:
        print(f"Deleted Customer {customer_id}")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    # print("1. Get all customers")
    # get_all_customers()
    
    # print("\n2. Get customer with ID 1")
    # get_customer(1)
    
    print("\n3. Add new customer")
    add_customer("Mohamed", "mohamed@example.com", 34)
    
    # print("\n4. Update customer with ID 1")
    # update_customer(1, "John Doe", "john.doe@newdomain.com", 31)
    
    # print("\n5. Delete customer with ID 1")
    # delete_customer(1)
    
    print("\n6. Get all customers after changes")
    get_all_customers()
