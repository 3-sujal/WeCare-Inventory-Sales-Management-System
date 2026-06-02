"""
Module for business operations (sales and restocking)
"""
from datetime import datetime  # Import for timestamp generation.
from read import read_products  # Import to read product data.
from write import write_invoice, save_products  # Import to write invoices and save product data.

def perform_sale(products):
    """
    Perform the sale of a product, update stock, and generate an invoice.

    Parameters:
        products (dict): Dictionary with product IDs as keys and product details as values

    Returns:
        dict: Updated products dictionary after sale
    
    Raises:
        ValueError: If input conversion fails or quantity is invalid
    """
    try:
        # Display header for bill generation.
        print("-------------------------------------------------------------------------------------------------------------")
        print("For Bill Generation you will have to enter your details first: ")
        print("-------------------------------------------------------------------------------------------------------------\n")

        # Get customer details.
        name = input("Please enter the name of the Customer: ")
        print("\n")
        phone_number = input("Please enter the phone number of the Customer: ")
        print("\n")

        total = 0  # Initialize total bill amount.
        current_time = datetime.now()  # Get current timestamp.
        # Initialize invoice text with customer details.
        invoice_text = "\nBill for " + name + "\nPhone: " + phone_number + "\nDate: " + str(current_time) + "\n"
        invoice_text += "-" * 100 + "\n"
        invoice_text += "Product \t Brand \t\tQuantity Sold \tFree \tPrice(each) \tTotal\n"

        sell_loop = True  # Control variable for sales loop.
        while sell_loop:
            # Display product list.
            print("*" * 80)
            print("id \t Name \t\t Brand \t\t Quantity \t Price \t Origin")
            print("*" * 80)

            for key in products:  # Iterate over products and display details.
                value = products[key]
                print(str(key) + "\t" + value[0] + "\t" + value[1] + "\t" + value[2] + "\t" + str(int(value[3]) * 2) + "\t" + value[4])

            try:
                # Get product ID and validate.
                product_id = int(input("Please Provide the ID of the product you want to sell: "))
                while product_id <= 0 or product_id not in products:
                    product_id = int(input("Invalid ID. Please enter a valid product ID as given in the list: "))

                # Get quantity and calculate free items (buy 2, get 1 free).
                product_quantity = int(input("Enter quantity to buy: "))
                free_items = product_quantity // 3
                total_quantity = product_quantity + free_items

                # Check stock availability.
                available_quantity = int(products[product_id][2])
                while product_quantity <= 0 or total_quantity > available_quantity:
                    print("Not enough stock. Please enter a valid quantity.")
                    product_quantity = int(input("Enter quantity to buy: "))
                    free_items = product_quantity // 3
                    total_quantity = product_quantity + free_items

                # Update stock.
                products[product_id][2] = str(available_quantity - total_quantity)

                # Calculate selling price (double the cost price) and total for the product.
                selling_price = int(products[product_id][3]) * 2
                product_total = selling_price * product_quantity
                total += product_total

                # Update invoice text with product details.
                invoice_text += (products[product_id][0] + "\t" + products[product_id][1] + "\t" + 
                                str(product_quantity) + "\t\t" + str(free_items) + "\t" + 
                                str(selling_price) + "\t\t" + str(product_total) + "\n")

                print("Dear " + name + ", you received " + str(free_items) + " free item(s) under our offer.")
                # Ask if the customer wants to buy more.
                cont = input("Do you want to buy more product? if yes type yes if no type no (yes/no): ").lower()
                if cont != 'yes':
                    sell_loop = False

            except ValueError:  # Handle invalid input.
                print("Invalid input. Please enter numeric values where required.")

        # Finalize invoice text with total amount.
        invoice_text += "-" * 100 + f"\nTotal Amount:\t\t\t\t\t\t\t\t{total}\n"
        print(invoice_text)

        # Save invoice and updated product data.
        write_invoice(invoice_text, transaction_type="sale")
        save_products(products)

        return products  # Return updated product dictionary.

    except Exception as errooor:  # Handle any unexpected errors.
        print(f"An error occurred: {errooor}")
        return products

def perform_restock(products):
    """
    Perform product restocking from supplier.
    """
    try:
        # Get supplier details.
        print("Please enter the Supplier details for restocking or if you don't know we can show the list just press any number:\n")
        supplier = input("Supplier name: ")
        # Initialize invoice text with supplier details.
        invoice = f"Restock from {supplier} on {datetime.now()}\n"
        invoice += "Product \t Brand \t\tQuantity \tPrice \tTotal\n"
        total_cost = 0  # Initialize total restock cost.

        restock_loop = True  # Control variable for restocking loop.
        while restock_loop:
            # Display product list.
            for key in products:
                value = products[key]
                print(str(key) + "\t" + value[0] + "\t" + value[1] + "\t" + value[2] + "\t" + value[3] + "\t" + value[4])

            # Get product ID and validate.
            product_id = int(input("Enter product ID to restock the product: "))
            while product_id <= 0 or product_id not in products:
                product_id = int(input("Invalid product ID. please enter the valid ID from the list "))

            # Get quantity and new price (if applicable).
            new_quantity = int(input("Enter quantity to add: "))
            new_price = int(input("Enter cost price (0 to skip): "))

            # Update product quantity and price.
            products[product_id][2] = str(int(products[product_id][2]) + new_quantity)
            if new_price > 0:
                products[product_id][3] = str(new_price)

            # Calculate total cost for the product.
            total = new_quantity * int(products[product_id][3])
            total_cost += total

            # Update invoice text with restock details.
            invoice += (products[product_id][0] + "\t" + products[product_id][1] + "\t" + 
                       str(new_quantity) + "\t\t" + products[product_id][3] + "\t" + 
                       str(total) + "\n")

            # Ask if more products need to be restocked.
            cont = input("Restock another product? (yes/no): ")
            if cont.lower() != 'yes':
                restock_loop = False

        # Finalize invoice text with total restock cost.
        invoice += f"\nTotal Restock Cost: {total_cost}"
        print(invoice)
        # Save invoice and updated product data.
        write_invoice(invoice, transaction_type="restock")
        save_products(products)

        return products  # Return updated product dictionary.
    except Exception as errorrestock:  # Handle any unexpected errors.
        print(f"Error during restocking: {errorrestock}")
        return products
