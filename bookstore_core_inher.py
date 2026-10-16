"""
This code is a refactoring of a previous system into a more organized structure using inheritance. 
The purpose of this code is to improve code reuse and make the system easier to manage.

Refactoring Details:
--------------------
1. Person Class: 
   - A base class that handles common attributes such as name, phone, and email.
   - Provides properties to retrieve these details.

2. Customer Class: 
   - Inherits from the `Person` class and extends its functionality specifically for customers. 
   - Uses the `super().__init__()` method to pass inherited attributes to the `Person` class.

3. Product Class: 
   - A base class for products, storing the product name and price.
   - Provides properties to retrieve these details.

4. Stock Class: 
   - Inherits from the `Product` class, adding an author attribute for books.
   - Provides additional methods to retrieve author information.

5. Order Class: 
   - Links a customer with a stock (book), creating a relationship between who is ordering and what they are ordering.
   - Provides properties to get customer and stock details.

6. Shipping Class: 
   - Handles shipping for orders, calculating shipping costs based on urgency.
   - Keeps track of the number of urgent shipments using a class-level counter.

7. Invoice Class: 
   - Combines the stock details and shipping costs to generate an invoice.
   - Stores the invoice number and calculates the total cost.

8. BookStore Class: 
   - Manages a list of invoices, providing methods to search for invoices.

9. Test Class:
   - Demonstrates how the system works by creating instances of customers, stocks, orders, shipping, and invoices.
   - Shows how everything interacts together to generate and manage invoices.

Overall, this refactoring introduces inheritance to streamline code, minimize redundancy, and make the system more extendable and maintainable.
"""

import datetime

class Person:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def get_name(self):
        return self.name

    @property
    def get_phone(self):
        return self.phone

    @property
    def get_email(self):
        return self.email


class Customer(Person):
    def __init__(self, name: str, phone: str, email: str):
        super().__init__(name, phone, email)


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def get_name(self):
        return self.name

    @property
    def get_price(self):
        return self.price


class Stock(Product):
    def __init__(self, name: str, author: str, price: float):
        super().__init__(name, price)
        self.author = author

    @property
    def get_author(self):
        return self.author


class Order:
    def __init__(self, customer: Customer, stock: Stock):
        self.customer = customer
        self.stock = stock

    @property
    def get_customer(self):
        return self.customer

    @property
    def get_stock(self):
        return self.stock


class Shipping:
    count_urgent = 0

    def __init__(self, order: Order, ship_date: datetime.date):
        self.order = order
        self.ship_date = ship_date
        self.ship_cost = 0.0

    @property
    def get_ship_date(self):
        return self.ship_date

    @property
    def get_ship_cost(self):
        return self.ship_cost

    def set_ship_cost(self, cost: float):
        self.ship_cost = cost

    def calc_ship_cost(self, is_urgent: bool):
        if is_urgent:
            self.ship_cost = 5.45
            Shipping.count_urgent += 1
        else:
            self.ship_cost = 3.95
        return self.ship_cost


class Invoice:
    def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping):
        self.invoice_nbr = invoice_nbr
        self.stock = stock
        self.ship_order = ship_order
        self.total_cost = 0.0

    @property
    def get_invoice_nbr(self):
        return self.invoice_nbr

    def invoice(self):
        self.total_cost = self.stock.get_price + self.ship_order.get_ship_cost
        return self.total_cost

# BookStore Class
class BookStore:
    def __init__(self):
        self.invoices = []

    @property
    def get_invoices(self):
        return self.invoices

    def search_invoice(self, nbr: str):
        for invoice in self.invoices:
            if invoice.get_invoice_nbr == nbr:
                return invoice
        print("Invoice not found")


class Test:
    def main():
        customer1 = Customer("david", "123456789", "david@example.com")
        customer2 = Customer("Bob", "987654321", "bob@example.com")
        customer3 = Customer("Charlie", "456123789", "charlie@example.com")

        stock1 = Stock("Book A", "Author A", 10.99)
        stock2 = Stock("Book B", "Author B", 15.50)
        stock3 = Stock("Book C", "Author C", 20.00)

        order1 = Order(customer1, stock1)
        order2 = Order(customer2, stock2)
        order3 = Order(customer3, stock3)

        shipping1 = Shipping(order1, datetime.date.today())
        shipping2 = Shipping(order2, datetime.date.today())
        shipping3 = Shipping(order3, datetime.date.today())

        shipping1.set_ship_cost(shipping1.calc_ship_cost(True))
        shipping2.set_ship_cost(shipping2.calc_ship_cost(False))
        shipping3.set_ship_cost(shipping3.calc_ship_cost(True))

        invoice1 = Invoice("INV0001", stock1, shipping1)
        invoice2 = Invoice("INV0002", stock2, shipping2)
        invoice3 = Invoice("INV0003", stock3, shipping3)

        bookstore = BookStore()
        bookstore.invoices.append(invoice1)
        bookstore.invoices.append(invoice2)
        bookstore.invoices.append(invoice3)

        print(f"Number of urgent shipments: {Shipping.count_urgent}")
        print(f"Invoice 1 total cost: {invoice1.invoice():.2f}")
        print(f"Invoice 2 total cost: {invoice2.invoice():.2f}")
        print(f"Invoice 3 total cost: {invoice3.invoice():.2f}")

        bookstore.search_invoice("INV0004")

if __name__ == "__main__":
    Test.main()