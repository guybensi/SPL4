from persistence import *

def print_activities():
    """Print the activities table ordered by date."""
    query = """
    SELECT product_id, quantity, activator_id, date
    FROM activities
    ORDER BY date;
    """
    results = repo.execute_command(query)
    for row in results:
        print(f"({row[0]}, {row[1]}, {row[2]}, '{row[3]}')")

def print_branches():
    """Print the branches table ordered by ID."""
    query = """
    SELECT id, location, number_of_employees
    FROM branches
    ORDER BY id;
    """
    results = repo.execute_command(query)
    for row in results:
        print(f"({row[0]}, '{row[1]}', {row[2]})")

def print_employees():
    """Print the employees table ordered by ID."""
    query = """
    SELECT id, name, salary, branche
    FROM employees
    ORDER BY id;
    """
    results = repo.execute_command(query)
    for row in results:
        print(f"({row[0]}, '{row[1]}', {row[2]}, {row[3]})")

def print_products():
    """Print the products table ordered by ID."""
    query = """
    SELECT id, description, price, quantity
    FROM products
    ORDER BY id;
    """
    results = repo.execute_command(query)
    for row in results:
        print(f"({row[0]}, '{row[1]}', {row[2]}, {row[3]})")

def print_suppliers():
    """Print the suppliers table ordered by ID."""
    query = """
    SELECT id, name, contact_information
    FROM suppliers
    ORDER BY id;
    """
    results = repo.execute_command(query)
    for row in results:
        print(f"({row[0]}, '{row[1]}', '{row[2]}')")

def print_employee_report():
    """Print a detailed employee report ordered by name."""
    query = """
    SELECT e.name, e.salary, b.location, 
           IFNULL(SUM(-a.quantity * p.price), 0) AS total_sales_income
    FROM employees e
    JOIN branches b ON e.branche = b.id
    LEFT JOIN activities a ON a.activator_id = e.id AND a.quantity < 0
    LEFT JOIN products p ON a.product_id = p.id
    GROUP BY e.id
    ORDER BY e.name;
    """
    results = repo.execute_command(query)
    for row in results:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]}")

def print_activity_report():
    """Print a detailed activity report ordered by date."""
    query = """
    SELECT a.date, p.description, a.quantity,
           CASE WHEN a.quantity < 0 THEN e.name ELSE NULL END AS seller_name,
           CASE WHEN a.quantity > 0 THEN s.name ELSE NULL END AS supplier_name
    FROM activities a
    JOIN products p ON a.product_id = p.id
    LEFT JOIN employees e ON a.activator_id = e.id AND a.quantity < 0
    LEFT JOIN suppliers s ON a.activator_id = s.id AND a.quantity > 0
    ORDER BY a.date;
    """
    results = repo.execute_command(query)
    for row in results:
        seller = f"'{row[3]}'" if row[3] else "None"
        supplier = f"'{row[4]}'" if row[4] else "None"
        print(f"('{row[0]}', '{row[1]}', {row[2]}, {seller}, {supplier})")

def main():
    print("Activities")
    print_activities()

    print("Branches")
    print_branches()

    print("Employees")
    print_employees()

    print("Products")
    print_products()

    print("Suppliers")
    print_suppliers()

    print("Employees report")
    print_employee_report()

    print("Activities report")
    print_activity_report()

if __name__ == '__main__':
    main()
