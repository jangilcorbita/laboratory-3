from models import Food, Beverage

class Menu:
    def __init__(self):
        self.menu = {
            "M1": Beverage("M1", "Pearl Milk Tea", 100.00),
            "M2": Beverage("M2", "Panda Milk Tea", 100.00),
            "M3": Beverage("M3", "Grass Jelly Milk Tea", 100.00),
            "M4": Beverage("M4", "White Pearl Milk Tea", 100.00),
            "M5": Beverage("M5", "2 Ladies Milk Tea", 110.00),
            "M6": Beverage("M6", "3 Buddies Milk Tea", 120.00),
            "M7": Beverage("M7", "Passion Fruit Tea Burst", 110.00),
            "M8": Food("M8", "Jumbo Fries", 117.00),
            "M9": Food("M9", "Mega Fries (2 Flavors)", 147.00),
            "M10": Food("M10", "Tera Fries (3 Flavors)", 257.00),
        }

    def view_menu(self):
        print("\n")
        print("Menu")
        for menu_id, item in self.menu.items():
            print(f"[{menu_id}] {item.name} - ₱{item.price:.2f}")