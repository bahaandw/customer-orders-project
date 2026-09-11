# Customer Orders Project

A simple Python project that loads customer and order data, combines the datasets, calculates business metrics, and saves the results as JSON files.

## Features

- Loads customer data from a JSON file
- Loads order data from a CSV file
- Creates a customer lookup dictionary using customer IDs
- Combines customer and order information
- Calculates:
  - Total revenue
  - Average order value
  - Revenue by customer
  - Revenue by city
  - Units sold by product
  - Top customer
  - Top city
  - Best-selling products
- Saves processed data and reports as JSON files

## Files

- `customers.json` - Customer information
- `orders.csv` - Order information
- Python script - Processes the data and generates the reports

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Replace `main.py` with the name of your Python file if it is different.

## Technologies Used

- Python
- CSV
- JSON
- `collections.defaultdict`

## Purpose

This project was created to practise working with files, lists, dictionaries, functions, data transformation, and basic data analysis in Python.