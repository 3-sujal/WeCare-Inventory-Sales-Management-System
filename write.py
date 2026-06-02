# write.py

from datetime import datetime  # Import datetime module for timestamp generation.

"""
Write invoice text to a uniquely named .txt file.

Parameters:
    invoice_text (str): The full invoice string to write.
    transaction_type (str): Type of transaction ("sale" or "restock").

Returns:
    None

Raises:
    IOError: If file writing fails.
"""

def write_invoice(invoice_text, transaction_type="sale"):
    try:
        current_time = datetime.now()  # Get current timestamp.
        # Generate a unique filename using transaction type and timestamp.
        filename = transaction_type + "_invoice_" + str(current_time).replace(" ", "_").replace(":", "") + ".txt"
        with open(filename, "w") as f:  # Open the file in write mode.
            f.write(invoice_text)  # Write the invoice text to the file.
    except IOError:  # Handle file writing errors.
        print("An error occurred while writing the invoice file.")

def save_products(products):
    """
    Save product data back to products.txt file.
    
    Parameters:
        products (dict): The products dictionary to save.
    """
    try:
        with open("products.txt", "w") as f:  # Open the file in write mode.
            for v in products.values():  # Iterate over each product in the dictionary.
                f.write(",".join(v) + "\n")  # Write product details as a comma-separated string.
    except Exception as errorsaving:  # Handle any errors during file saving.
        print(f"Error saving products: {errorsaving}")
