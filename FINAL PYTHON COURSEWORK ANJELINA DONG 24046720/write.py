import time 
'''
Updates the new list of product dictionaries into a text file. Every product goes on a new line in the following format:
name,brand,quantity,cost_price,origin

Parameters:
products (list): A list of dictionaries. Each dictionary represents a product with keys:
                   'name', 'brand', 'quantity', 'cost_price', and 'origin'.
filename (str): The file name where product data will be written to. Default is "products.txt".
 Returns:
 None (The function writes to a file but does not return any value.)
'''

def write_products(products, filename="products.txt"):

    try:
        file = open(filename, "w")
        for product in products:
            line = product["name"] + "," + product["brand"] + "," + str(product["quantity"]) + "," + str(product["cost_price"]) + "," + product["origin"] + "\n"
            file.write(line)
        file.close()
    except IOError:
        print("Error: Unable to write to file", filename)

'''
 Generates a purchase invoice file containing customer details, purchased items,
  quantities (including free items), prices, and the total amount.

 Parameters:
   customer_name (str): The name of the customer making the purchase.
   items       (list): A list of dictionaries, each representing a purchased item with keys:
                         'name', 'brand', 'final_quantity', 'selling_price', and 'subtotal'.
   total       (float): The total bill amount for the entire purchase.

 Returns:
  None (The function writes an invoice to a file but does not return any value.)

'''
def write_purchase_invoice(customer_name, items, total):

    filename = "invoice_purchase_" + customer_name + ".txt"
    try:
        file = open(filename, "w")
        file.write("Purchase Invoice\n")
        file.write("Customer Name: " + customer_name + "\n")
        file.write("Date: [Generated at time of transaction]\n")
        file.write("---------------------------------\n")
        for item in items:
            file.write("Product: " + item["name"] + "\n")
            file.write("Brand: " + item["brand"] + "\n")
            file.write("Quantity (including free): " + str(item["final_quantity"]) + "\n")
            file.write("Unit Price: " + str(item["selling_price"]) + "\n")
            file.write("Subtotal: " + str(item["subtotal"]) + "\n")
            file.write("---------------------------------\n")
        file.write("Total Amount: " + str(total) + "\n")
        file.close()
    except IOError:
        print("Error: Could not write invoice file")

'''
  Generates a restock invoice file that includes vendor details, restocked items,
    quantities, cost prices, and the total restocking cost.

 Parameters:
   vendor_name (str): The name of the vendor who supplied the products.
   items       (list): A list of dictionaries, each representing a restocked item with keys:
                        'name', 'brand', 'quantity', 'cost_price', and 'subtotal'.
   total       (float): The total cost for all restocked items.

 Returns:
   None (The function writes an invoice to a file but does not return any value.)
'''
def write_restock_invoice(vendor_name, items, total):

    filename = "invoice_restock_" + vendor_name + ".txt"
    try:
        file = open(filename, "w")
        file.write("Restock Invoice\n")
        file.write("Vendor Name: " + vendor_name + "\n")
        file.write("Date: [Generated at time of transaction]\n")
        file.write("---------------------------------\n")
        for item in items:
            file.write("Product: " + item["name"] + "\n")
            file.write("Brand: " + item["brand"] + "\n")
            file.write("Quantity Restocked: " + str(item["quantity"]) + "\n")
            file.write("Cost Price per Unit: " + str(item["cost_price"]) + "\n")
            file.write("Subtotal: " + str(item["subtotal"]) + "\n")
            file.write("---------------------------------\n")
        file.write("Total Amount: " + str(total) + "\n")
        file.close()
    except IOError:    #deals with a case in which the file cannot be opened or written. This could occur if the file is locked or if the disk is full or there is a problem of permission.
        print("Error: Could not write restock invoice file")
