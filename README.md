# Bookstore Ordering System (Python)

A bookstore ordering system that manages customers, stock, orders, shipping and invoices, with a Tkinter desktop interface.

## What it does

- Record **customers** and **books in stock**
- Create **orders** linking a customer to a book
- Calculate **shipping**, with a higher charge for urgent delivery and a running count of urgent shipments
- Produce an **invoice** totalling the book price and shipping cost

## Files

| File | Purpose |
|---|---|
| `bookstore_core.py` | The core classes: Customer, Stock, Order, Shipping, Invoice |
| `bookstore_core_inher.py` | A refactored version using inheritance (`Person` → `Customer`, `Product` → `Stock`) to remove duplication |
| `bookstore_gui.py` | Tkinter desktop interface built on the inheritance version |

## Run it

Requirements: Python 3.10 or later (Tkinter is included with standard Python).

```bash
python bookstore_gui.py
```
