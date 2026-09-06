from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def process(self):
        pass


class CashPayment(Payment):
    def process(self):
        return f"Cash payment of ₱{self._amount:.2f} received"


class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self._card_number = card_number

    def process(self):
        return f"Card payment of ₱{self._amount:.2f} received"


class Delivery:
    def __init__(self, order):
        self.order = order
        self.status = "Preparing"

    def update_status(self, status):
        self.status = status


class Transaction:
    def __init__(self, order, payment, delivery):
        self.order = order
        self.payment = payment
        self.delivery = delivery
        self.payment_status = "Completed"


class PaymentDeliveryManager:
    def __init__(self):
        self.transactions = {}

    def process_order(self, order_manager):
        print("\nProcess Payment and Delivery")
        order_id = input("Enter Order ID: ").upper()

        if order_id not in order_manager.orders:
            print("Order not found.")
            return

        if order_id in self.transactions:
            print("Order has already been processed.")
            return

        order = order_manager.orders[order_id]
        method = input("Payment method (cash/card): ").lower()

        if method == "card":
            card_number = input("Enter Card Number: ")
            payment = CardPayment(order.total, card_number)
        else:
            payment = CashPayment(order.total)

        delivery = Delivery(order)
        transaction = Transaction(order, payment, delivery)
        self.transactions[order_id] = transaction
        order.status = "Paid"

        print(payment.process())
        print(f"Delivery for {order_id} is {delivery.status}.")

    def update_delivery(self):
        print("\nUpdate Delivery")
        order_id = input("Enter Order ID: ").upper()

        if order_id not in self.transactions:
            print("Transaction not found.")
            return

        status = input("Enter delivery status (Preparing/In Transit/Delivered): ")
        transaction = self.transactions[order_id]
        transaction.delivery.update_status(status)
        transaction.order.status = status
        print(f"Delivery for {order_id} updated to {status}.")

    def manage_payment_and_delivery(self, order_manager):
        print("\nPayment and Delivery")
        print("1. Process Payment")
        print("2. Update Delivery")
        choice = input("Select an option: ")

        if choice == "1":
            self.process_order(order_manager)
        elif choice == "2":
            self.update_delivery()

    def view_completed_transactions(self):
        print("\nCompleted Transactions")

        if not self.transactions:
            print("No completed transactions.")
            return

        for order_id, transaction in self.transactions.items():
            print(
                f"{order_id} | {transaction.order.customer.name} | "
                f"₱{transaction.payment._amount:.2f} | "
                f"Payment: {transaction.payment_status} | "
                f"Delivery: {transaction.delivery.status}"
            )