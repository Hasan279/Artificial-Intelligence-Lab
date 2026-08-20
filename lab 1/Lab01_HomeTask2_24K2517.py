def compute_units_cost(units):
    if units <= 100:
        cost = units * 12
    elif units <= 300:
        cost = (100 * 12) + ((units - 100) * 18)
    else:
        cost = (100 * 12) + (200 * 18) + ((units - 300) * 25)
    return cost

def compute_bill(units, tax_rate=0.17, fixed_charge=150):
    slab_cost = compute_units_cost(units)
    tax = slab_cost * tax_rate
    total = slab_cost + tax + fixed_charge
    
    print("Units:", units)
    print("Slab Cost:", slab_cost)
    print("Tax:", round(tax, 2))
    print("Fixed Charge:", fixed_charge)
    print("Total Payable:", round(total, 2))
    print()
    return total

val = input("Enter units: ")

if not val.replace('.', '', 1).isdigit() or float(val) < 0:
    print("Invalid input! Please enter a non-negative number.")
else:
    units = float(val)
    if units.is_integer():
        units = int(units)

    print("Bill 1 (Defaults):")
    compute_bill(units)

    print("Bill 2 (Keyword tax_rate):")
    compute_bill(units, tax_rate=0.20)

    print("Bill 3 (Overriding both):")
    compute_bill(units, tax_rate=0.10, fixed_charge=200)
