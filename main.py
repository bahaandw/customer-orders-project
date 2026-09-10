import csv
import json
from collections import defaultdict

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
        processed_order = {
            'customer_id': customer_id, 
            'customer_name': customer_name, 
            'city': city, 
            'product': product, 
            'quantity': quantity, 
            'price': price, 
            'total': total}
        processed_orders.append(processed_order)
    return processed_orders

processed_orders = process_orders(orders, customers_by_id)
print(f"First line of processed orders: {processed_orders[0]}")

# Calculate total revenue of all orders
def calculate_total_revenue(processed_orders):
    total_revenue = 0
    for processed_order in processed_orders:
        total_revenue += processed_order['total']
    return total_revenue

# Calculate revenue by customer and store it in a dictionary
def calculate_revenue_by_customer(processed_orders):
    revenue_by_customer = defaultdict(int)
    for processed_order in processed_orders:
        customer_name = processed_order['customer_name']
        total = processed_order['total']
        revenue_by_customer[customer_name] += total
    return dict(revenue_by_customer)

revenue_by_customer = calculate_revenue_by_customer(processed_orders)
print(f"Revenue by customer: {revenue_by_customer}")

# Calculate revenue by city and store it in a dictionary
def calculate_revenue_by_city(processed_orders):
    revenue_by_city = defaultdict(int)
    for processed_order in processed_orders:
        city = processed_order['city']
        total = processed_order['total']
        revenue_by_city[city] += total
    return dict(revenue_by_city)

revenue_by_city = calculate_revenue_by_city(processed_orders)
print(f"Revenue by city: {revenue_by_city}")

# Calculate units sold by product and store it in a dictionary
def calculate_units_by_product(processed_orders):
    units_by_product = defaultdict(int)
    for processed_order in processed_orders:
        product = processed_order['product']
        quantity = processed_order['quantity']
        units_by_product[product] += quantity
    return dict(units_by_product)

units_by_product = calculate_units_by_product(processed_orders)
print(f"Units by product: {units_by_product}")

# Calculate average order value
def calculate_average_order_value(processed_orders):
    total_order_value = 0
    number_of_orders = 0
    for processed_order in processed_orders:
        number_of_orders += 1
        order_value = processed_order['price'] * processed_order['quantity']
        total_order_value += order_value
    average_order_value = total_order_value / number_of_orders
    return average_order_value

average_order_value = calculate_average_order_value(processed_orders)
print(f"Average order value: {average_order_value}")


# Combine the results of the business metrics into one final report dictionary
def build_report(processed_orders):     
    total_revenue = calculate_total_revenue(processed_orders)
    average_order_value = calculate_average_order_value(processed_orders)
    revenue_by_customer = calculate_revenue_by_customer(processed_orders)
    top_customer = max(revenue_by_customer, key=revenue_by_customer.get)  # Returns the key which corresponds to the highest value
    revenue_by_city = calculate_revenue_by_city(processed_orders)
    top_city = max(revenue_by_city, key=revenue_by_city.get)
    units_by_product = calculate_units_by_product(processed_orders)
    max_units = max(units_by_product.values()) # Since multiple products have a tie we need to find the max value first
    best_selling_products = [k for k in units_by_product if units_by_product[k] == max_units] # Loop through each product and if its value matches the max we add it to the list of best-selling products
    final_report = {
        'total_revenue': total_revenue,
        'average_order_value': average_order_value,
        'top_customer': top_customer,
        'top_city': top_city,
        'best_selling_products': best_selling_products
    }
    return final_report

final_report = build_report(processed_orders)
print(f"Final report: {final_report}")

def save_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

save_json(final_report, 'final_report.json')
save_json(processed_orders, 'processed_orders.json')
