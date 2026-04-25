# Arrays Assessment
# Author: Mars Angelo P. Buñao

# Parallel arrays for product names and prices
product_names = []
product_prices = []

def add_product():
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        product_names.append(name)
        product_prices.append(price)
        print(f"{name} added successfully!\n")
    except ValueError:
        print("Invalid price. Please enter a number.\n")

def display_products():
    if not product_names:
        print("No products available.\n")
        return
    print("\n--- Product List ---")
    for i in range(len(product_names)):
        print(f"{i + 1}. {product_names[i]} - ₱{product_prices[i]:.2f}")
    print()

def search_product():
    search = input("Enter product name to search: ")
    if search in product_names:
        index = product_names.index(search)
        print(f"Product found: {product_names[index]} - ₱{product_prices[index]:.2f}\n")
    else:
        print("Product not found.\n")

def update_price():
    name = input("Enter product name to update price: ")
    if name in product_names:
        index = product_names.index(name)
        try:
            new_price = float(input("Enter new price: "))
            product_prices[index] = new_price
            print(f"Price for {name} updated to ₱{new_price:.2f}\n")
        except ValueError:
            print("Invalid price input.\n")
    else:
        print("Product not found.\n")

def total_price():
    if not product_prices:
        print("No products to calculate.\n")
        return
    total = sum(product_prices)
    print(f"Total price of all products: ₱{total:.2f}\n")

def menu():
    while True:
        print("=== Product Inventory Menu ===")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Search Product")
        print("4. Update Product Price")
        print("5. Show Total Price")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_price()
        elif choice == "5":
            total_price()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
