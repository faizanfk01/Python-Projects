from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using credit card."

class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."

payments = [CreditCard(), PayPal()]

for payment in payments:
    print(payment.pay(100))