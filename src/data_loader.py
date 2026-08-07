import pandas as pd

def load_data():
    customers = pd.read_csv("data/raw/customers.csv")
    orders = pd.read_csv("data/raw/orders.csv")
    order_items = pd.read_csv("data/raw/order_items.csv")
    products = pd.read_csv("data/raw/products.csv")

    return customers, orders, order_items, products