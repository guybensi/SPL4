from persistence import *

import sys

def process_action(splittedline):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    activator_id = int(splittedline[2])
    date = splittedline[3]

    # Retrieve the product
    product = repo.products.find(id=product_id)
    if not product:
        return

    product = product[0]

    if quantity < 0:  # Sale
        if product.quantity + quantity < 0:
            return
        product.quantity += quantity

    elif quantity > 0:  # Supply
        product.quantity += quantity

    # Update the product quantity in the database
    repo.products.update(product)

    # Insert the activity
    activity = Activitie(product_id=product_id, quantity=quantity, activator_id=activator_id, date=date)
    repo.activities.insert(activity)
    repo._conn.commit()



def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            process_action(splittedline)
if __name__ == '__main__':
    main(sys.argv)