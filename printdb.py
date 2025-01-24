from persistence import *

def print_activities():
    """Print the activities table ordered by date."""
    activities = repo.activities.find_all()
    for activity in sorted(activities, key=lambda a: a.date):
        print(activity)

def print_branches():
    """Print the branches table ordered by ID."""
    branches = repo.branches.find_all()
    for branch in sorted(branches, key=lambda b: b.id):
        print(branch)

def print_employees():
    """Print the employees table ordered by ID."""
    employees = repo.employees.find_all()
    for employee in sorted(employees, key=lambda e: e.id):
        print(employee)

def print_products():
    """Print the products table ordered by ID."""
    products = repo.products.find_all()
    for product in sorted(products, key=lambda p: p.id):
        print(product)

def print_suppliers():
    """Print the suppliers table ordered by ID."""
    suppliers = repo.suppliers.find_all()
    for supplier in sorted(suppliers, key=lambda s: s.id):
        print(supplier)

def print_employee_report():
    """Print a detailed employee report ordered by name."""
    employees = repo.employees.find_all()
    employees = sorted(employees, key=lambda e: e.name)
    for employee in employees:
        # Calculate total sales income
        total_sales_income = sum(
            abs(activity.quantity) * repo.products.find(id=activity.product_id)[0].price
            for activity in repo.activities.find(activator_id=employee.id)
            if activity.quantity < 0
        )
        branch = repo.branches.find(id=employee.branche)[0]
        print(f"{employee.name} {employee.salary} {branch.location} {total_sales_income}")

def print_activity_report():
    """Print a detailed activity report ordered by date."""
    activities = sorted(repo.activities.find_all(), key=lambda a: a.date)
    for activity in activities:
        product = repo.products.find(id=activity.product_id)[0]
        if activity.quantity > 0:  # Supply
            supplier = repo.suppliers.find(id=activity.activator_id)[0]
            print(f"('{product.description}', {activity.quantity}, None, '{supplier.name}', '{activity.date}')")
        else:  # Sale
            employee = repo.employees.find(id=activity.activator_id)[0]
            print(f"('{product.description}', {activity.quantity}, '{employee.name}', None, '{activity.date}')")

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
