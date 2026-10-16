"""
This code is a simple bookstore system that keeps track of customers, books, orders, shipping, 
and invoices. It uses different classes to organize everything and make it easier to manage. 
Here’s what each part does:

Classes:

1. Customer:
   - Represents a person buying a book.
   - Stores their name, phone number, and email address.
   - Lets you look up these details.

2. Stock:
   - Represents a book in the store.
   - Stores the book’s name, author, and price.
   - Lets you see these details.

3. Order:
   - Connects a customer to a book they want to buy.
   - Lets you check which customer ordered which book.

4. Shipping:
   - Handles how the order is shipped.
   - Stores the shipping date and calculates the shipping cost.
   - If it’s urgent, the cost is higher. Also counts how many urgent shipments there are.

5. Invoice:
   - Represents the bill for an order.
   - Adds up the book’s price and the shipping cost to show the total.
   - Keeps track of the invoice number.

6. BookStore:
   - Keeps a list of all the invoices.
   - Lets you search for a specific invoice by its number.

7. Test:
   - A demo class that shows how everything works together.
   - Creates example customers, books, orders, shipping details, and invoices.
   - Calculates shipping costs and total prices.
   - Shows how to search for an invoice.

"""

import datetime


class Customer:
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


class Stock:
    def __init__(self, book_name: str, author: str, price: float):
        self.book_name = book_name
        self.author = author
        self.price = price

    @property
    def get_book_name(self):
        return self.book_name

    @property
    def get_author(self):
        return self.author

    @property
    def get_price(self):
        return self.price


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