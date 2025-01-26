from persistence import *
import sys
import os

def add_branch(splittedline):
    """Add a branch record to the database."""
    repo.branches.insert(Branche(id=int(splittedline[0]), location=splittedline[1], number_of_employees=int(splittedline[2])))

def add_supplier(splittedline):
    """Add a supplier record to the database."""
    repo.suppliers.insert(Supplier(id=int(splittedline[0]), name=splittedline[1], contact_information=splittedline[2]))

def add_product(splittedline):
    """Add a product record to the database."""
    repo.products.insert(Product(id=int(splittedline[0]), description=splittedline[1], price=float(splittedline[2]), quantity=int(splittedline[3])))

def add_employee(splittedline):
    """Add an employee record to the database."""
    repo.employees.insert(Employee(id=int(splittedline[0]), name=splittedline[1], salary=float(splittedline[2]), branche=int(splittedline[3])))

adders = {  "B": add_branch,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")

    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            #not menatory, validaty check
            if (splittedline[0] in adders):
                adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)