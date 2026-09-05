from menu import Menu

class FoodDeliverySystem:
    def __init__(self):
        self.menu_manager = Menu()

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
                ...
            elif choice == '2': 
                self.menu_manager.view_menu()
            elif choice == '3': 
                ...
            elif choice == '4':
                ...
            elif choice == '5':
                ...
            elif choice == '6': 
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = FoodDeliverySystem()
    app.run()