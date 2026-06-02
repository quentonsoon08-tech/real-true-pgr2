# main.py - Stationery Inventory Management System (Main Script)
# Module: Programming 2 (SF43002FP)
# Description: Provides an interactive menu for managing stationery inventory.
#              Users can add, edit, update sold items, display all items,
#              and save the inventory to a CSV file.
#
# Data types used : int (quantity, counter), float (price, total_price),
#                   str (name, filename, user input, menu text)
# Keywords used   : while True, if, elif, else, break, continue,
#                   def, for, class (in stationery.py), True, False
 
import os
import csv
from stationery import StationeryItem   # Import the StationeryItem class
 
 
# -------------------------------------------------------
# INVENTORY LIST
# Stores all stationery items as dictionaries inside a list
# Each dictionary has four keys:
#   "name"        -> str   e.g. "Pen"
#   "quantity"    -> int   e.g. 200
#   "price"       -> float e.g. 1.20
#   "total_price" -> float e.g. 240.00
# -------------------------------------------------------
inventory = []   # empty list - items will be added below
 
# Sample data from Table 1
# Each row: [str name, int quantity, float price]
sample_items = [
    ["Pen",          200, 1.20],
    ["Pencil",       250, 0.80],
    ["Eraser",       150, 0.50],
    ["Glue Stick",   100, 1.10],
    ["Writing Book", 300, 1.50],
]
 
# Use a for loop to load every sample row into the inventory list
for row in sample_items:
    item_name     = str(row[0])    # str  - item name
    item_quantity = int(row[1])    # int  - quantity in stock
    item_price    = float(row[2])  # float - unit price
 
    # Create a StationeryItem object to calculate total price
    item_obj   = StationeryItem(item_name, item_quantity, item_price)
    item_total = item_obj.calculate_total()   # float - quantity x price
 
    # Build a dictionary for this item and add it to the inventory list
    inventory.append({
        "name":        item_name,      # str
        "quantity":    item_quantity,  # int
        "price":       item_price,     # float
        "total_price": item_total      # float
    })
 
 
# -------------------------------------------------------
# def clear_screen - clears the terminal display
# -------------------------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
 
 
# -------------------------------------------------------
# def display_menu - prints the main menu options (str)
# -------------------------------------------------------
def display_menu():
    print("====================================================")
    print("     STATIONERY INVENTORY MANAGEMENT SYSTEM")
    print("====================================================")
    print("  1 - To enter new stationery item")
    print("  2 - To edit the stationery item")
    print("  3 - To update the stationery item which was sold")
    print("  4 - To display all the stationery items")
    print("  5 - To save the list of all stationery items in .CSV file")
    print("====================================================")
 
 
# -------------------------------------------------------
# def find_item - searches the inventory list by name (str)
# Returns the matching item dictionary, or None if not found
# Demonstrates: for, if, break
# -------------------------------------------------------
def find_item(name):
    # name parameter is a str - the item name to search for
    found_item = None   # start as None (not found)
 
    for item in inventory:
        # item["name"] is str - compare both in lowercase for case-insensitive search
        if item["name"].lower() == name.lower():
            found_item = item
            break   # item found - stop searching
 
    return found_item   # returns a dict if found, or None if not found
 
 
# -------------------------------------------------------
# def get_valid_quantity - keeps asking until the user
# enters a valid whole number (int), 0 or greater
# Demonstrates: while True, if, continue, break, int, str
# -------------------------------------------------------
def get_valid_quantity(prompt):  # That prompt is the string is usually the message shown to the user, like "Enter the price:"
    # prompt is a str - the message shown to the user
    valid    = False    # bool flag - becomes True when input is accepted
    quantity = 0        # int - will hold the final valid quantity
 
    while True:
        user_input = input(prompt)   # user_input is a str (raw keyboard input)
 
        # Check if the user typed nothing
        if user_input == "":    # str comparison
            print("  [!] Input cannot be empty. Please try again.")
            continue   # loop back and ask again
 
        # Try to convert the str input into an int
        try:
            quantity = int(user_input)   # int conversion from str
        except ValueError:
            # Conversion failed - user typed letters or symbols
            print("  [!] Invalid input. Please enter a whole number (e.g. 100).")
            continue   # loop back and ask again
 
        # Quantity (int) must not be negative
        if quantity < 0:    # int comparison
            print("  [!] Quantity cannot be negative. Please try again.")
            continue   # loop back
 
        # All checks passed - input is a valid int
        valid = True    # bool - mark as accepted
        break           # exit the while True loop
 
    return quantity   # int
 
 
# -------------------------------------------------------
# def get_valid_price - keeps asking until the user
# enters a valid decimal number (float), 0.00 or greater
# Demonstrates: while True, if, continue, break, float, str
# -------------------------------------------------------
def get_valid_price(prompt): 
    # prompt is a str - the message shown to the user
    valid = False   # bool flag
    price = 0.0     # float - will hold the final valid price
 
    while True:
        user_input = input(prompt)   # user_input is a str
 
        # Check if input is empty str
        if user_input == "":    # str comparison
            print("  [!] Input cannot be empty. Please try again.")
            continue   # loop back
 
        # Try to convert the str input into a float
        try:
            price = float(user_input)   # float conversion from str
        except ValueError:
            print("  [!] Invalid input. Please enter a number with decimals (e.g. 1.50).")
            continue   # loop back
 
        # Price (float) must not be negative
        if price < 0.0:     # float comparison
            print("  [!] Price cannot be negative. Please try again.")
            continue   # loop back
 
        # All checks passed
        valid = True    # bool
        break           # exit the while True loop
 
    return price   # float
 
 
# -------------------------------------------------------
# def get_valid_name - keeps asking until the user enters
# a name that contains letters only (spaces allowed).
# Numbers, decimals, symbols, and special characters
# are all rejected.
# Demonstrates: while True, if, elif, else, for, continue, break
# -------------------------------------------------------
def get_valid_name(prompt):
    # prompt is a str - the message shown to the user
 
    while True:
        name = input(prompt).strip()   # str - raw input with leading/trailing spaces removed
 
        # Check 1: name must not be empty
        if name == "":   # str comparison
            print("  [!] Item name cannot be empty. Please try again.")
            continue   # loop back and ask again
 
        # Check 2: name must only contain letters and spaces (no digits or symbols)
        # Use a for loop to check every single character in the name
        name_is_valid = True   # bool flag - assume valid until a bad character is found
 
        for character in name:   # for loop - goes through each character one by one
            # character.isalpha() returns True if the character is a letter (A-Z or a-z)
            # character == " " allows spaces between words e.g. "Glue Stick"
            if character.isalpha() == False and character != " ":
                # Found a character that is NOT a letter and NOT a space
                # This catches digits (0-9), decimals (.), symbols (@, #, !, etc.)
                name_is_valid = False   # bool - mark as invalid
                break   # no need to check the remaining characters
 
        # Check the result of the for loop above
        if name_is_valid == False:
            print("  [!] Invalid name. Item name must contain letters only.")
            print("      Numbers, decimals, and symbols are not allowed.")
            continue   # loop back and ask the user to try again
 
        # Check 3: name must not be only spaces (e.g. user typed "   ")
        if name.replace(" ", "") == "":   # remove all spaces and check if anything is left
            print("  [!] Item name cannot be blank spaces only. Please try again.")
            continue   # loop back
 
        # All checks passed - name contains only letters (and spaces between words)
        break   # exit the while True loop
 
    return name   # str - the validated item name
 
 
# -------------------------------------------------------
# def option1_add_item - Option 1: Add a new stationery item
# Collects str name, int quantity, float price from the user
# Uses StationeryItem class to calculate float total_price
# -------------------------------------------------------
def option1_add_item():
    print("\n--- ADD NEW STATIONERY ITEM ---")
 
    # Get item name using the helper function
    # Only letters and spaces are accepted - numbers and symbols are rejected
    name = get_valid_name("Enter item name: ")   # str - validated letters-only name
 
    # Check if this str name already exists in inventory
    if find_item(name) != None:
        print("  [!] '" + name + "' already exists. Use Option 2 to edit it.")
        return   # stop and go back to menu
 
    # Get valid quantity (int) using helper function
    # Loop until user enters a quantity greater than 0
    # A quantity of 0 is not allowed when adding a new item
    while True:
        quantity = get_valid_quantity("Enter quantity: ")   # int - must be > 0 for new items
        if quantity == 0:   # int comparison - reject zero stock when adding new item
            print("  [!] Quantity must be greater than 0 when adding a new item.")
            continue   # loop back and ask again
        break   # valid int greater than 0 - exit loop
 
    # Get valid price (float) using helper function
    # Loop until user enters a price greater than $0.00
    # A price of 0.00 is not allowed when adding a new item
    while True:
        price = get_valid_price("Enter price ($): ")   # float - must be > 0.00 for new items
        if price == 0.0:   # float comparison - reject zero price when adding new item
            print("  [!] Price must be greater than $0.00 when adding a new item.")
            continue   # loop back and ask again
        break   # valid float greater than 0.00 - exit loop
 
    # Create a StationeryItem object and calculate total price (float)
    item_obj   = StationeryItem(name, quantity, price)
    total      = item_obj.calculate_total()   # float = int x float
 
    # Store the new item as a dictionary with str, int, float values
    new_item = {
        "name":        name,      # str
        "quantity":    quantity,  # int
        "price":       price,     # float
        "total_price": total      # float
    }
    inventory.append(new_item)
 
    # str() converts int and float to str for printing
    print("\n  [OK] '" + name + "' added successfully!")
    print("       Total Price: $" + str(total))   # float converted to str
 
 
# -------------------------------------------------------
# def option2_edit_item - Option 2: Edit an existing item
# Finds item by str name, prompts for new str/int/float values
# -------------------------------------------------------
def option2_edit_item():
    print("\n--- EDIT STATIONERY ITEM ---")
 
    # Get str name to search for
    name = input("Enter the name of the item to edit: ").strip()   # str
 
    item = find_item(name)   # returns dict or None
 
    # If not found, display error message (str) and return
    if item == None:
        print("  [!] Error: '" + name + "' not found in inventory.")
        return
 
    # Display current details - converting int and float to str for printing
    print("\n  Current details:")
    print("    Name     : " + str(item["name"]))          # str
    print("    Quantity : " + str(item["quantity"]))       # int -> str
    print("    Price    : $" + str(item["price"]))         # float -> str
    print("    Total    : $" + str(item["total_price"]))   # float -> str
    print("  (Press Enter to keep the current value)\n")
 
    # --- Edit name (str) ---
    new_name = input("  New name [" + str(item["name"]) + "]: ").strip()   # str
    if new_name == "":      # str comparison - empty means keep old value
        new_name = item["name"]   # str - keep existing name
 
    # --- Edit quantity (int) ---
    qty_prompt = "  New quantity [" + str(item["quantity"]) + "]: "  # str prompt
    qty_input  = input(qty_prompt).strip()   # str raw input
 
    if qty_input == "":     # str comparison - empty means keep old value
        new_qty = item["quantity"]   # int - keep existing quantity
    else:
        new_qty = 0   # int placeholder
        while True:
            try:
                new_qty = int(qty_input)    # convert str to int
            except ValueError:
                print("  [!] Invalid input. Please enter a whole number.")
                qty_input = input(qty_prompt).strip()   # str - ask again
                continue   # loop back to re-validate
 
            if new_qty < 0:     # int comparison
                print("  [!] Quantity cannot be negative.")
                qty_input = input(qty_prompt).strip()   # str
                continue   # loop back
            else:
                break   # valid int - exit loop
 
    # --- Edit price (float) ---
    price_prompt = "  New price [$" + str(item["price"]) + "]: "   # str prompt
    price_input  = input(price_prompt).strip()   # str raw input
 
    if price_input == "":   # str comparison - empty means keep old value
        new_price = item["price"]   # float - keep existing price
    else:
        new_price = 0.0   # float placeholder
        while True:
            try:
                new_price = float(price_input)   # convert str to float
            except ValueError:
                print("  [!] Invalid input. Please enter a number (e.g. 1.50).")
                price_input = input(price_prompt).strip()   # str
                continue   # loop back
 
            if new_price < 0.0:     # float comparison
                print("  [!] Price cannot be negative.")
                price_input = input(price_prompt).strip()   # str
                continue   # loop back
            else:
                break   # valid float - exit loop
 
    # Recalculate total_price (float) using StationeryItem class
    item_obj  = StationeryItem(new_name, new_qty, new_price)
    new_total = item_obj.calculate_total()   # float
 
    # Update the dictionary with new str, int, float values
    item["name"]        = new_name    # str
    item["quantity"]    = new_qty     # int
    item["price"]       = new_price   # float
    item["total_price"] = new_total   # float
 
    print("\n  [OK] '" + str(new_name) + "' updated successfully!")
    print("       New Total Price: $" + str(new_total))   # float -> str
 
 
# -------------------------------------------------------
# def option3_update_sold - Option 3: Deduct sold quantity
# Takes str name and int sold_qty, updates int quantity
# and recalculates float total_price
# -------------------------------------------------------
def option3_update_sold():
    print("\n--- UPDATE SOLD STATIONERY ---")
 
    # Get str name of the item that was sold
    name = input("Enter the name of the sold item: ").strip()   # str
 
    item = find_item(name)   # returns dict or None
 
    if item == None:
        print("  [!] Error: '" + name + "' not found in inventory.")
        return
 
    # Display current int quantity and float price as str
    print("  Current stock - Quantity: " + str(item["quantity"]) +
          " | Price: $" + str(item["price"]))
 
    # Keep asking until a valid int sold quantity is entered
    sold_qty = 0    # int placeholder
    while True:
        sold_input = input("  Enter quantity sold: ")   # str raw input
 
        # Try to convert str input to int
        try:
            sold_qty = int(sold_input)   # int conversion from str
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")
            continue   # loop back
 
        # sold_qty (int) must be greater than 0
        if sold_qty <= 0:   # int comparison
            print("  [!] Quantity sold must be more than 0.")
            continue   # loop back
 
        # Cannot sell more than current stock (int comparison)
        elif sold_qty > item["quantity"]:
            print("  [!] Cannot sell more than current stock (" +
                  str(item["quantity"]) + ").")   # int -> str
            continue   # loop back
 
        else:
            break   # valid int - exit loop
 
    # Deduct int sold_qty from int quantity
    item["quantity"] = item["quantity"] - sold_qty   # int - int = int
 
    # Recalculate float total_price using StationeryItem
    item_obj          = StationeryItem(item["name"], item["quantity"], item["price"])
    item["total_price"] = item_obj.calculate_total()   # float
 
    print("\n  [OK] Sale recorded!")
    print("       Remaining stock of '" + str(item["name"]) + "': " +
          str(item["quantity"]))                        # int -> str
    print("       Updated Total Price: $" + str(item["total_price"]))   # float -> str
 
 
# -------------------------------------------------------
# def option4_display_all - Option 4: Display all items
# Prints a formatted table using str, int, and float values
# Demonstrates: for loop, int counter, float grand_total
# -------------------------------------------------------
def option4_display_all():
    print("\n--- ALL STATIONERY ITEMS ---\n")
 
    # len() returns an int - number of items in inventory
    if len(inventory) == 0:   # int comparison
        print("  (No items in inventory.)")
        return
 
    # Print str table header
    print("  " + "-" * 62)
    print("  {:<5} {:<18} {:>10} {:>12} {:>12}".format(
          "No.", "Name", "Quantity", "Price ($)", "Total ($)"))
    print("  " + "-" * 62)
 
    # int counter to number each row
    counter = 1   # int
 
    for item in inventory:
        # item["name"] is str, item["quantity"] is int,
        # item["price"] and item["total_price"] are float
        print("  {:<5} {:<18} {:>10} {:>12.2f} {:>12.2f}".format(
              counter,               # int
              item["name"],          # str
              item["quantity"],      # int
              item["price"],         # float (shown with 2 decimal places)
              item["total_price"]))  # float (shown with 2 decimal places)
 
        counter = counter + 1   # int + int = int, increment row number
 
    print("  " + "-" * 62)
 
    # Calculate float grand total by summing all float total_price values
    grand_total = 0.0   # float - start at zero
    for item in inventory:
        grand_total = grand_total + item["total_price"]   # float + float = float
 
    print("  {:<5} {:<18} {:>10} {:>12} {:>12.2f}".format(
          "", "GRAND TOTAL", "", "", grand_total))   # float shown with 2 decimal places
    print()
 
 
# -------------------------------------------------------
# def option5_save_csv - Option 5: Save inventory to CSV
# Writes str, int, and float values to a .csv file
# filename is a str; each row contains str, int, float data
# -------------------------------------------------------
def option5_save_csv():
    filename = "stationery_inventory.csv"   # str - name of the output file
 
    # Try to open (or create) the CSV file for writing
    try:
        csv_file = open(filename, mode="w", newline="")   # str filename
    except IOError:
        print("\n  [!] Error: Could not open file for writing.")
        return
 
    # Write the str header row to the CSV file
    csv_file.write("No.,Name,Quantity,Price ($),Total Price ($)\n")   # str
 
    # int counter to number each row in the CSV
    counter = 1   # int
 
    for item in inventory:
        # Build each CSV row as a str by converting int and float to str
        row = (str(counter) + "," +           # int -> str
               str(item["name"]) + "," +      # str
               str(item["quantity"]) + "," +  # int -> str
               str(item["price"]) + "," +     # float -> str
               str(item["total_price"]) + "\n")  # float -> str
 
        csv_file.write(row)    # write the str row to the file
        counter = counter + 1  # int increment
 
    csv_file.close()
 
    # filename is a str - shown in the success message
    print("\n  [OK] Inventory saved to '" + filename + "' successfully!")   # str
 
 
# -------------------------------------------------------
# def ask_continue - asks user to enter Y or N (str input)
# Returns True (bool) to continue, or False (bool) to exit
# Demonstrates: while True, if, elif, else, break, str
# -------------------------------------------------------
def ask_continue():
    while True:
        # choice is a str - user types Y or N
        choice = input("\nDo you want to continue? (Y/N): ").strip().upper()   # str
 
        if choice == "Y":       # str comparison
            clear_screen()
            return True         # bool - keep the program running
        elif choice == "N":     # str comparison
            return False        # bool - stop the program
        else:
            # Any other str input is invalid
            print("  [!] Invalid input. Please enter Y or N.")
 
 
# -------------------------------------------------------
# MAIN PROGRAM - entry point of the application
# -------------------------------------------------------
def main():
    clear_screen()
 
    # while True keeps the menu running until the user exits
    while True:
        display_menu()
 
        # option is a str - whatever the user types
        option = input("\nEnter your option (1-5): ").strip()   # str
 
        # Compare str option to str menu choices using if / elif / else
        if option == "1":       # str comparison
            option1_add_item()
 
        elif option == "2":     # str comparison
            option2_edit_item()
 
        elif option == "3":     # str comparison
            option3_update_sold()
 
        elif option == "4":     # str comparison
            option4_display_all()
 
        elif option == "5":     # str comparison
            option5_save_csv()   # call option5_save_csv() to save the inventory to a CSV file
 
        else:
            # option is a str that does not match any valid choice
            print("\n  [!] Invalid option '" + option +
                  "'. Please select 1, 2, 3, 4 or 5.")   # str
 
        # ask_continue returns a bool (True or False)
        keep_going = ask_continue()   # bool
 
        if keep_going == False:   # bool comparison
            print("\n  Thank you for using the Stationery Inventory Management System. Goodbye!\n")  # print a goodbye message
            break   # exit the while True loop and end the program
 
 
# Run main() only when this script is executed directly
if __name__ == "__main__":  # check if this file is being run directly
    main()   # call main() to start the program
