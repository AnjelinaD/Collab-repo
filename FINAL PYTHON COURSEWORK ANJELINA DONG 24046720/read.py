#read.py
#stores by keeping the list inside the dictionary

'''
The main Function is display_products

Summary:
 Displays a neatly formatted table of all products from the products list.
 Each product is shown with its number, name, brand, quantity, price (double the cost price), and origin.

Parameters:
products (list): A list of dictionaries. Each dictionary describes a product with keys:
                   'name', 'brand', 'quantity', 'cost_price', and 'origin'.
Returns:
  None (This function only prints the product information on the screen.)
'''

def display_products(products):
       
    print("Available Products:\n")

    print("-----|---------------------|------------------|---------|-------|-----------------------|")
    print("No.  | Name                | Brand            | Quantity| Price | Origin                |")
    print("-----|---------------------|------------------|---------|-------|-----------------------|")

    index = 1
    for product in products:
        name = product["name"]
        brand = product["brand"]
        quantity = str(product["quantity"])
        price = str(int(product["cost_price"] * 2))
        origin = product["origin"]

        index_str = str(index)                 # Padding to align table columns properly
        name_space = " " * (20 - len(name))
        brand_space = " " * (17 - len(brand))
        quantity_space = " " * (8 - len(quantity))
        price_space = " " * (6 - len(price))
        origin_space = " " * (22 - len(origin))

        row = index_str + "    | " + name + name_space + "| " + brand + brand_space + "| " + quantity + quantity_space + "| " + price + price_space + "| " + origin + origin_space + "|"
        print(row)

        index = index + 1


'''
The Function is read_products

Summary:
Reads product information from the text file and stores it in a list of dictionaries.
 Each product line must have name, brand, quantity, cost_price, and origin separated by commas.

 Parameters:
   filename (str): The name of a file to read from. Default is "products.txt"

 Returns:
   list: A list of dictionaries. Each dictionary contains:
         'name', 'brand', 'quantity' (int), 'cost_price' (float), and 'origin'.
'''
def read_products(filename="products.txt"):

    products = []
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if line != "\n":    #Empty line is skipped  
                parts = line.split(",")
                if len(parts) == 5:
                    origin_value = parts[4]
                    if origin_value.endswith("\n"):
                        origin_value = origin_value[:-1]  # helps in removing newline manually

                    product = {
                        "name": parts[0],
                        "brand": parts[1],
                        "quantity": int(parts[2]),
                        "cost_price": float(parts[3]),
                        "origin": origin_value
                    }
                    products.append(product)
                else:
                    print("Skipping malformed line:", line)
    except IOError:
        print("Error: Could not open the file", filename)
    except Exception as e:
        print("An error occurred while reading the file:", e)
    

    return products
