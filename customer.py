from models import Customer

class CustomerManager:
    def __init__(self):
        self.customers = {}

    def register_customer(self):
        print("\n")
        print("Register New Customer")
        customer_id = input("Enter Customer ID: ")
        
        if customer_id in self.customers:
            print("Customer ID already exists!")
            return
        
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Delivery Address: ")

        new_customer = Customer(customer_id, name, phone, address)
        self.customers[customer_id] = new_customer
        
        print(f"Customer {name} registered successfully.")