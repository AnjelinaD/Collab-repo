import read
import write
import datetime

'''Function for the purchase of a product.
This function receives a list of products as an input, gives the user an option to select products and quantities.
and sends a purchase invoice adding all the amount. The purpose also guarantees availability of stock
and uses free-item policy (after every third item purchased free item is provided).

Parameters in operations.py:
products (list): A list of product dictionaries and in each there will be the details of the product.
(e.g., name, brand, cost_price, quantity).

 Returns:
None. The function creates a purchase invoice and updates stock of products.'''

def purchase_product(products):

    customer = input("Enter customer name: ")
    cart = []  #Declaring an empty cart which will store the purchased items
    total = 0  #Seting the initial price of all purchased items

    while True:
        read.display_products(products) #Displaying the products that can be purchased.
        try:
            choice = int(input("Enter product number to purchase (press 0 to end): "))
            if choice == 0:
                break       #If 0 is entered then exit the loop
            if choice < 1 or choice > len(products):
                print("Invalid choice.") #ensuring correct product selection
                continue

            quantity = int(input("Enter quantity to purchase: "))
            product = products[choice - 1]   #Get chosen product details
            free_items = quantity // 3       #Calculating free products from the purchase quantity 
            total_items = quantity + free_items  #Total items including the free ones 

            if product["quantity"] < total_items: #checking if sufficient stock is available  
                print("Not enough stock. Free item policy requires more stock.")
                continue

            selling_price = product["cost_price"] * 2  #setting selling price as twice the cost price
            subtotal = quantity * selling_price       #calculating subtotal for this product
            total += subtotal                         #Adding into the final purchase amount
            product["quantity"] -= total_items        #Stock is updated after buying

            cart.append({                             #Adding product purchase details to the cart
                "name": product["name"],
                "brand": product["brand"],
                "final_quantity": total_items,
                "selling_price": selling_price,
                "subtotal": subtotal
            })

        except ValueError:                            #handles invalid input
            print("Invalid input. Please try again.")

    if len(cart) > 0:                                 #If items are placed on the cart, then the invoice is  produced and presented
        write.write_purchase_invoice(customer, cart, total)
        write.write_products(products)

        print("\n----------* Purchase Invoice *----------")
        print("Customer Name:", customer)
        date=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day)
        print("Date:", date)                            #Displaying the current date
        print("---------------------------------")

        for item in cart:                                #Displaying details of each item in the cart
            print("Product:", item["name"])
            print("Brand:", item["brand"])
            print("Quantity (including free):", item["final_quantity"])
            print("Unit Price:", item["selling_price"])
            print("Subtotal:", item["subtotal"])
            print("---------------------------------")

        print("Total Amount:", total)                     #Displaying the total amount of the pruchase
        print("Purchase has been completed. Invoice is generated.") 


'''Function for restocking of products 
This function enables the user to enter or update products in the inventory and gives a restock invoice.
It adds new goods if the product is not already within the list and updates the stocks of the existing products.

Parameters: products (list): A list of product dictionaries, with each dictionary having product details.
returns: None. The function creates a restock invoice and updates products’ stock.
'''

def restock_product(products):

    vendor = input("Enter vendor's name: ")
    cart = []
    total = 0

    while True:
        try:
            name = input("Enter product name (or type 'end' to finish): ")
            if name.lower() == "end":
                break

            brand = input("Enter brand: ")
            quantity = int(input("Enter quantity to restock: "))
            cost = float(input("Enter cost price per unit: ")) #Cost price per unit
            origin = input("Enter country of origin: ")

            found = False  #Uisng Boolean to check if the product already exists or not
            for each in products:
                if each["name"].lower()==name.lower():  #Checking if product already exists
                    each["quantity"]=int(each["quantity"])+quantity  #updating the quantity
                    each["cost_price"]=cost                          #updating the cost price
                    store=each["brand"]
                    found=True                                       #if the product is dound
            
                    
                

            subtotal = cost * quantity                              #Calculating subtotal for the restock

            if found==False:                                         #If the product is new then adding it to the product list
                new_product = {
                    "name": name,
                    "brand": brand,
                    "quantity": quantity,
                    "cost_price": cost,
                    "origin": origin
                }
                products.append(new_product)
                print(f"Added new product: {name} ({brand})")

            total += subtotal                                          #Adding to the total restock cost
            cart.append({
                "name": name,
                "brand": brand,
                "quantity": quantity,
                "cost_price": cost,
                "subtotal": subtotal
            })

        except ValueError:
            print("Invalid input. Please enter valid numbers for quantity and cost.")   #Handling invalid input

    if len(cart) > 0:          #If the products were restocked teh generating and displaying the restock invoice
        write.write_restock_invoice(vendor, cart, total)  #Write the restock invoice to a file
        write.write_products(products)                  #Write updated product list to a file

        print("\n*-------- Restock Invoice --------*")
        print("Vendor Name:", vendor)
        date=str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day)
        
        print("Date:", date)
        
        print("---------------------------------")

        for item in cart:
            print("Product:", item["name"])
            if found==False:
                print("Brand:", new_product["brand"])
            else:
                print("Brand:", store)
            print("Quantity Restocked:", item["quantity"])
            print("Cost Price per Unit:", item["cost_price"])
            print("Subtotal:", item["subtotal"])
            print("---------------------------------")

        print("Total Amount:", total)
        print("Restock complete. Invoice has been generated!")
