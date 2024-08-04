# Initialize the inventory dictionary
shop = {
    'chair': [10, 10000],
    'sofa-set': [5, 60000],
    'table': [7, 15000],
    'bed': [3, 40000],
}

total_income = 0

while True:
    product_name = input("Enter the product name (or 'exit' to quit): ").strip().lower()
    if product_name == 'exit':
        break

    if product_name in shop and shop[product_name][0] > 0:
        quantity, price = shop[product_name]
        print(f"Product: {product_name}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")
        
        quantity_sold = int(input(f"Enter the quantity of {product_name} sold: "))
        
        if quantity >= quantity_sold:
            shop[product_name][0] -= quantity_sold
            income = quantity_sold * price
            total_income += income
            print(f"Income from this sale: {income}")
            print(f"Updated inventory: {shop[product_name][0]} {product_name}(s) left.\n")
        else:
            print(f"Insufficient quantity of {product_name}. Only {quantity} available.\n")
    else:
        print(f"{product_name} is not available in the inventory or out of stock.\n")

print(f"Total income made by the owner: {total_income}")
