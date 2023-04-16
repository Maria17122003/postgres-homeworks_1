import psycopg2
import csv
import os

customers_data = os.path.join('north_data', 'customers_data.csv')
employees_data = os.path.join('north_data', 'employees_data.csv')
orders_data = os.path.join('north_data', 'orders_data.csv')

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="17122003M"
)

cur = conn.cursor()
with open(customers_data) as file:
    file_csv = csv.DictReader(file)
    for item in file_csv:
        cur.execute(
                    "INSERT INTO customers_data VALUES (%s, %s, %s)",
                    (item['customer_id'], item['company_name'], item['contact_name'])
                    )

with open(employees_data) as file:
    file_csv = csv.DictReader(file)
    for item in file_csv:
        cur.execute(
                    "INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s)",
                    (item['first_name'], item['last_name'], item['title'], item['birth_date'],
                     item['notes'])
                    )

with open(orders_data) as file:
    file_csv = csv.DictReader(file)
    for item in file_csv:
        cur.execute(
                    "INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)",
                    (item['order_id'], item['customer_id'], item['employee_id'], item['order_date'],
                     item['ship_city'])
                    )

conn.commit()
cur.close()
conn.close()
