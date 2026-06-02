# main.py

from read import read_products  # Import function to read product data.
from operations import perform_sale, perform_restock  # Import functions for sales and restocking.

"""
Main entry point for the WeCare system. Loops until admin exits.
"""

# Display welcome message and system header.
print("\n\n\t \t \t \t \tWeCare Wholesale\n")
print("\t \t \t \t \tKathmandu | Nepal")
print("-----------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t Welcome to the system Admin!")
print("---------------------------------------------------------------------------------------------------------------------------\n")

products = read_products()  # Load product data from file.
main_loop = True  # Control variable for the main loop.

while main_loop:
    # Display menu options.
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Given below are some of the options for you to carry out the needed operations:")
    print("-----------------------------------------------------------------------------------------------------------------------\n")
    print("Press 1 to sale the product to costumer.")
    print("Press 2 to purchase from Manufacturer.")
    print("Press 3 to Exit from the system.\n")
    print("-----------------------------------------------------------------------------------------------------------------------\n")

    try:
        options = int(input("Enter the option to continue: "))  # Get user input for menu selection.
        print("\n")

        if options == 1:
            products = perform_sale(products)  # Call function to handle sales.
        elif options == 2:
            products = perform_restock(products)  # Call function to handle restocking.
        elif options == 3:
            main_loop = False  # Exit the loop.
            print("Thank you for using the system, have a good day Admin!\n")
        else:
            print("Invalid option. Please try again.\n")

    except ValueError:  # Handle invalid input (non-integer).
        print("Please enter a valid number option.\n")
