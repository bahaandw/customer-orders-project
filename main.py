import csv
import json

#Function to load customer data from a JSON file
def load_customers(filename):
    with open(filename, 'r') as customer_file:
        customer_data = json.load(customer_file)
        return customer_data

#Function to load order data from a CSV file
def load_orders(filename):
    with open(filename, 'r') as order_file:
        order_data = csv.DictReader(order_file)
        order_data_list = []
        for row in order_data:
            order_data_list.append(row)
        return order_data_list

#Checking the first rows for both files
customer_data = load_customers('customers.json')
print(f"First line of customer data: {customer_data[0]}")

order_data = load_orders('orders.csv')
print(f"First line of order data: {order_data[0]}")

