from models import Order

class OrderManager:
    def __init__(self):
        self.orders = {}
        self.order_counter = 1

    def create_order(self, customer_manager, menu_manager):
        print("\n")
        print("Create New Order")
        
        customer_id = input("Enter Customer ID: ")
        if customer_id not in customer_manager.customers:
            print("Customer not found! Please register first.")
            return

        customer = customer_manager.customers[customer_id]

        order_items = []
        while True:
            item_id = input("Enter Menu Item ID (or 'done' to finish): ").upper()
            if item_id == 'DONE':
                break
            
            if item_id in menu_manager.menu:
                order_items.append(menu_manager.menu[item_id])
                print(f"Added: {menu_manager.menu[item_id].name}")
            else:
                print("Item ID not found in menu.")

        if not order_items:
            print("Order cannot be empty.")
            return

        order_id = f"ORDER#{self.order_counter:03d}"
        new_order = Order(order_id, customer)
        for item in order_items:
            new_order.add_item(item)

        self.orders[order_id] = new_order
        self.order_counter += 1

        print(f"\n{order_id} created successfully! Total: ₱{new_order.total:.2f}")