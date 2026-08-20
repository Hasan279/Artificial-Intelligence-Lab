inventory = {
    'GPU workstation': (4, 'good'),
    'Arduino kit': (10, 'fair'),
    'Raspberry Pi': (6, 'good')
}

def add_item(name, quantity, condition='good'):
    inventory[name] = (quantity, condition)
    print("Added", name)

def update_quantity(name, new_qty):
    if name in inventory:
        # tuples cannot be modified in place, so rebuilding the tuple with new quantity
        old_qty, condition = inventory[name]
        inventory[name] = (new_qty, condition)
        print("Updated quantity for", name)
    else:
        print("Item not found!")

def delete_item(name):
    if name in inventory:
        del inventory[name]
        print("Deleted", name)
    else:
        print("Item not found!")

def search_item(name):
    if name in inventory:
        qty, cond = inventory[name]
        print("Found:", name, "-> Quantity:", qty, ", Condition:", cond)
    else:
        print("Item not found!")

def list_all():
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    print("\n--- Current Inventory ---")
    conditions = set()
    for item in inventory:
        qty, cond = inventory[item]
        conditions.add(cond)
        print("Item:", item, "| Quantity:", qty, "| Condition:", cond)
    print("Unique Conditions:", conditions)

while True:
    print("\n1. Add item")
    print("2. Update quantity")
    print("3. Delete item")
    print("4. Search item")
    print("5. List everything")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == '1':
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        cond = input("Enter condition (press enter for default): ")
        if cond.strip() == "":
            add_item(name, qty)
        else:
            add_item(name, qty, cond)

    elif choice == '2':
        name = input("Enter item name: ")
        qty = int(input("Enter new quantity: "))
        update_quantity(name, qty)

    elif choice == '3':
        name = input("Enter item name to delete: ")
        delete_item(name)

    elif choice == '4':
        name = input("Enter item name to search: ")
        search_item(name)

    elif choice == '5':
        list_all()

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
