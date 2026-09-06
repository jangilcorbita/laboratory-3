from customer import CustomerManager
from menu import Menu
from order import OrderManager
from payment_delivery import PaymentDeliveryManager

class FoodDeliverySystem:
    def __init__(self):
        self.customer_manager = CustomerManager()
        self.menu_manager = Menu()
        self.order_manager = OrderManager()
        self.payment_delivery_manager = PaymentDeliveryManager()

    def run(self):
        while True:
            print("\n")
            print("Food Delivery System")
            print("1. Register Customer")
            print("2. View Menu")
            print("3. Create Order")
            print("4. Process Payment and Delivery")
            print("5. View Completed Transactions")
            print("6. Exit")
            print("\n")
            
            choice = input("Select an option: ")

            if choice == '1': 
                self.customer_manager.register_customer()
            elif choice == '2': 
                self.menu_manager.view_menu()
            elif choice == '3': 
                self.order_manager.create_order(self.customer_manager, self.menu_manager)
            elif choice == '4':
                self.payment_delivery_manager.manage_payment_and_delivery(
                    self.order_manager
                )
            elif choice == '5':
                self.payment_delivery_manager.view_completed_transactions()
            elif choice == '6': 
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = FoodDeliverySystem()
    app.run()