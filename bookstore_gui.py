"""
This is a graphical user interface (GUI) application for a book ordering system using tkinter. 
It allows users to manage customers, books, orders, shipping, and invoices in a bookstore setting.

The application uses object-oriented principles and interacts with a core module (bookstore_core_inher) that handles customer, stock, order, shipping, and invoice management. 


The main features of the application are:

1. Customer Management:
   - Users can add customers by entering their name, phone, and email.
   - The customer list is stored, and a dropdown is available for selecting customers when placing an order.

2. Book Management:
   - Users can add books to stock by entering the book's name, author, and price.
   - The book list is stored, and a dropdown is available for selecting books when placing an order.

3. Order Placement:
   - Users can place an order by selecting a customer and a book from the dropdowns.
   - Orders are stored for further actions (e.g., shipping, invoicing).

4. Shipping Calculation:
   - Users can calculate shipping costs based on the urgency of the shipment (urgent or regular).
   - Shipping costs are displayed to the user.

5. Invoice Generation:
   - After an order is placed and shipping is calculated, users can generate an invoice.
   - Invoices are automatically numbered and saved, showing the total cost (book price + shipping cost).

6. Invoice Search and View:
   - Users can search for an invoice by its number.
   - A list of all invoices can be viewed, showing the invoice number and total cost for each.


The GUI is built using tkinter's `LabelFrame`, `Entry`, `Button`, and `Combobox` widgets to create forms for entering data and displaying information. 
It also uses messageboxes for notifications and alerts.

"""
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from tkinter import BooleanVar
from bookstore_core_inher import Customer, Stock, Order, Shipping, Invoice, BookStore


class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Ordering System")
        self.customers = []
        self.stock = []
        self.orders = []
        self.bookstore = BookStore()
        self.current_order = None
        self.shipping_cost = 0.0

        self.create_widgets()

    def create_widgets(self):
        # Customer Input Form
        customer_frame = tk.LabelFrame(self.root, text="Customer Input Form")
        customer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(customer_frame, text="Name").grid(row=0, column=0)
        tk.Label(customer_frame, text="Phone").grid(row=1, column=0)
        tk.Label(customer_frame, text="Email").grid(row=2, column=0)

        self.customer_name = tk.Entry(customer_frame)
        self.customer_name.grid(row=0, column=1)
        self.customer_phone = tk.Entry(customer_frame)
        self.customer_phone.grid(row=1, column=1)
        self.customer_email = tk.Entry(customer_frame)
        self.customer_email.grid(row=2, column=1)

        tk.Button(customer_frame, text="Add Customer", command=self.add_customer).grid(row=3, column=0, columnspan=2)

        # Book Input Form
        book_frame = tk.LabelFrame(self.root, text="Book Input Form")
        book_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(book_frame, text="Book Name").grid(row=0, column=0)
        tk.Label(book_frame, text="Author").grid(row=1, column=0)
        tk.Label(book_frame, text="Price").grid(row=2, column=0)

        self.book_name = tk.Entry(book_frame)
        self.book_name.grid(row=0, column=1)
        self.book_author = tk.Entry(book_frame)
        self.book_author.grid(row=1, column=1)
        self.book_price = tk.Entry(book_frame)
        self.book_price.grid(row=2, column=1)

        tk.Button(book_frame, text="Add Book to Stock", command=self.add_stock).grid(row=3, column=0, columnspan=2)

        # Order Placement
        order_frame = tk.LabelFrame(self.root, text="Place Order")
        order_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(order_frame, text="Select Customer").grid(row=0, column=0)
        tk.Label(order_frame, text="Select Book").grid(row=1, column=0)

        self.customer_dropdown = ttk.Combobox(order_frame, state="readonly")
        self.customer_dropdown.grid(row=0, column=1)
        self.book_dropdown = ttk.Combobox(order_frame, state="readonly")
        self.book_dropdown.grid(row=1, column=1)

        tk.Button(order_frame, text="Place Order", command=self.place_order).grid(row=2, column=0, columnspan=2)

        # Shipping Options
        shipping_frame = tk.LabelFrame(self.root, text="Shipping Options")
        shipping_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.is_urgent = BooleanVar()
        tk.Checkbutton(shipping_frame, text="Urgent Shipping", variable=self.is_urgent).grid(row=0, column=0, columnspan=2)

        tk.Button(shipping_frame, text="Calculate Shipping", command=self.calculate_shipping).grid(row=1, column=0, columnspan=2)

        # Invoice Actions
        invoice_frame = tk.LabelFrame(self.root, text="Invoice Actions")
        invoice_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        tk.Button(invoice_frame, text="Generate Invoice", command=self.generate_invoice).grid(row=0, column=0, columnspan=2)

        tk.Label(invoice_frame, text="Invoice Number").grid(row=1, column=0)
        self.invoice_number = tk.Entry(invoice_frame)
        self.invoice_number.grid(row=1, column=1)

        tk.Button(invoice_frame, text="Search Invoice", command=self.search_invoice).grid(row=2, column=0, columnspan=2)
        tk.Button(invoice_frame, text="View All Invoices", command=self.view_all_invoices).grid(row=3, column=0, columnspan=2)

    def add_customer(self):
        name = self.customer_name.get()
        phone = self.customer_phone.get()
        email = self.customer_email.get()

        if name and phone and email:
            customer = Customer(name, phone, email)
            self.customers.append(customer)
            self.customer_dropdown['values'] = [c.get_name for c in self.customers]
            messagebox.showinfo("Success", f"Customer {name} added successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def add_stock(self):
        name = self.book_name.get()
        author = self.book_author.get()

        try:
            price = float(self.book_price.get())
            stock = Stock(name, author, price)
            self.stock.append(stock)
            self.book_dropdown['values'] = [b.get_name for b in self.stock]
            messagebox.showinfo("Success", f"Book {name} added successfully!")
        except ValueError:
            messagebox.showwarning("Input Error", "Price must be a valid number!")

    def place_order(self):
        customer_index = self.customer_dropdown.current()
        book_index = self.book_dropdown.current()

        if customer_index == -1 or book_index == -1:
            messagebox.showwarning("Selection Error", "Please select a customer and a book!")
            return

        customer = self.customers[customer_index]
        stock = self.stock[book_index]
        self.current_order = Order(customer, stock)
        messagebox.showinfo("Success", "Order placed successfully!")

    def calculate_shipping(self):
        if not self.current_order:
            messagebox.showwarning("Order Error", "Place an order first!")
            return

        shipping = Shipping(self.current_order, date.today())
        self.shipping_cost = shipping.calc_ship_cost(self.is_urgent.get())
        messagebox.showinfo("Shipping Calculated", f"Shipping Cost: ${self.shipping_cost:.2f}")

    def generate_invoice(self):
        if not self.current_order:
            messagebox.showwarning("Order Error", "Place an order first!")
            return

        if self.shipping_cost == 0:
            messagebox.showwarning("Shipping Error", "Calculate shipping cost first!")
            return

        invoice_number = f"INV{len(self.bookstore.get_invoices) + 1:04d}"
        shipping = Shipping(self.current_order, date.today())
        shipping.set_ship_cost(self.shipping_cost)
        invoice = Invoice(invoice_number, self.current_order.get_stock, shipping)

        self.bookstore.invoices.append(invoice)
        messagebox.showinfo("Invoice Generated", f"Invoice {invoice_number} generated successfully!")

    def search_invoice(self):
        invoice_number = self.invoice_number.get()
        invoice = self.bookstore.search_invoice(invoice_number)

        if invoice:
            messagebox.showinfo("Invoice Found", f"Invoice {invoice_number}:\nTotal Cost: ${invoice.invoice():.2f}")
        else:
            messagebox.showwarning("Not Found", "Invoice not found!")

    def view_all_invoices(self):
        invoices = self.bookstore.get_invoices
        if not invoices:
            messagebox.showinfo("No Invoices", "No invoices available.")
            return

        all_invoices = "\n".join([f"{inv.get_invoice_nbr}: ${inv.invoice():.2f}" for inv in invoices])
        messagebox.showinfo("All Invoices", all_invoices)


if __name__ == "__main__":
    root = tk.Tk()
    app = BookstoreApp(root)
    root.mainloop()
