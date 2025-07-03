# main.py

import read
import operations

def main():

    '''
        This is the starting point of WeCare Skin Care Product System.

        This function displays welcome message, provides menu to the users to either restock or pruchase the given products from the inventory or exit the system.

        The program  continuously loops until the user chooses to exit'''
    

    #Displays a welcome message

    print("                          ***Welcome to WeCare Skin Care Product System***")
    print("                                        Since 2025")
    
    #Reads product data from file

    products = read.read_products()
    
    #Loop has been created for main menu 

    while True:
        print("\nPlease choose an option to purchase or restock products:")
        print("1. Display/Purchase Products")
        print("2. Restock Products")
        print("3. Exit")

        #Gets user's input  

        choice = input("Choose options from(1-3): ")

        #Handles the user's choice 

        if choice == "1":
            operations.purchase_product(products) #Calls the function to handle product purchase 
        elif choice == "2":
            operations.restock_product(products) #Calls function to handle restocking products 
        elif choice == "3":
            print("Thank you for using WeCare System.")
            break
        else:
            print("Invalid option! Please choose again.") #Handles the invalid input

#calls the main function to run the program 

main()
