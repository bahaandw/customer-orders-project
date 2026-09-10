import csv
import json

# Function to load customer data from a JSON file
def load_customers(filename):
    with open(filename, 'r') as customer_file:
        customer_data = json.load(customer_file)
        return customer_data

# Function to load order data from a CSV file
def load_orders(filename):
    with open(filename, 'r') as order_file:
        order_data = csv.DictReader(order_file)
        order_data_list = []
        for row in order_data:
            order_data_list.append(row)
        return order_data_list

# Checking the first rows for both files
customers = load_customers('customers.json')
print(f"First line of customer data: {customers[0]}")

orders = load_orders('orders.csv')
print(f"First line of order data: {orders[0]}")

# Transform the customer list into a dictionary keyed by customer ID for more efficient lookups
def create_customer_lookup(customers):
    customers_by_id = {}
    for customer in customers:
        customers_by_id[int(customer['customer_id'])] = {'name': customer['name'], 'city': customer['city']}
    return customers_by_id

customers_by_id = create_customer_lookup(customers)
print(f"customers_by_id: {customers_by_id}")

# Function to combine the order and customer data into one list of dictionaries
def process_orders(orders, customers_by_id):
    processed_orders = []  # Processed orders list for combining orders with customers
    for order in orders:
        customer_id = int(order['customer_id'])
        customer_name = customers_by_id[customer_id]['name']    # Retrieve customer with corresponding customer_id
        city = customers_by_id[customer_id]['city'] 
        product = order['product']
        quantity = int(order['quantity']) # Cast quantity to integer
        price = float(order['price']) # Cast price to floating point number
        total = quantity * price # Calculate the total order price
        processed_order = {'customer_id': customer_id, 'customer_name': customer_name, 'city': city, 'product': product, 'quantity': quantity, 'price': price, 'total': total}
        processed_orders.append(processed_order)
    return processed_orders

processed_orders = process_orders(orders, customers_by_id)
print(f"First line of processed orders: {processed_orders[0]}")
