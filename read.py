# read.py

"""
Read product data from a text file and store it in a dictionary.

Parameters:
    None

Returns:
    dict: A dictionary with product ID as key and product info list as value.

Raises:
    FileNotFoundError: If 'products.txt' file is not found.
"""

def read_products():
    dictonary = {}  # Initialize an empty dictionary to store product data.
    try:
        file = open("products.txt", "r")  # Open the file in read mode.
        data = file.readlines()  # Read all lines from the file into a list.
        pro_id = 1  # Initialize product ID counter.
        for line in data:  # Iterate over each line in the file.
            line = line.replace("\n", "").split(",")  # Remove newline and split by comma to get product details.
            dictonary[pro_id] = line  # Add product details to the dictionary with p_id as the key.
            pro_id += 1  # Increment product ID for the next product.
        file.close()  # Close the file after reading.
    except FileNotFoundError:  # Handle case where file is not found.
        print("The file 'products.txt' was not found.")
    return dictonary  # Return the populated dictionary.
