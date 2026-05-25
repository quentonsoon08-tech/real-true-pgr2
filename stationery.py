# stationery.py - Companion Script for Stationery Inventory Management System
# Module: Programming 2 (SF43002FP)
# Description: Defines the StationeryItem class with methods to store item
#              details and calculate the total price (quantity x price).
#              This script is imported by main.py.
#
# Data types used : int (quantity), float (price, total_price), str (name, status)
# Keywords used   : class, def, if, elif, else, for, while True, break, continue,
#                   True, False
 
 
# -------------------------------------------------------
# CLASS definition - used to create StationeryItem objects
# -------------------------------------------------------
class StationeryItem:
 
    # def __init__ runs when a new StationeryItem object is created
    # It stores the item's name, quantity, and price
    def __init__(self, name, quantity, price):
 
        self.name     = str(name)       # str  - name of the stationery item e.g. "Pen"
        self.quantity = int(quantity)   # int  - number of units in stock e.g. 200
        self.price    = float(price)    # float - unit price in dollars e.g. 1.20
        self.is_valid = False           # bool - False until validate() says data is ok
 
    # -------------------------------------------------------
    # def validate - checks that quantity and price are valid
    # Returns True if all values are acceptable, False if not
    # Demonstrates: while True, if, elif, else, break, continue, True, False
    # -------------------------------------------------------
    def validate(self):
 
        # while True loops until we break out with a result
        while True:
 
            # quantity must be 0 or more (int)
            if self.quantity < 0:
                self.is_valid = False
                break   # exit loop - invalid quantity, no need to check price
 
            # price must be 0.00 or more (float)
            if self.price < 0.0:
                self.is_valid = False
                break   # exit loop - invalid price
 
            # name must not be an empty string (str)
            if self.name == "":
                self.is_valid = False
                break   # exit loop - name cannot be blank
 
            # All checks passed - item data is valid
            self.is_valid = True
            break   # exit the while True loop
 
        return self.is_valid
 
    # -------------------------------------------------------
    # def calculate_total - multiplies quantity (int) by
    # price (float) and returns total_price (float)
    # -------------------------------------------------------
    def calculate_total(self):
 
        # quantity is an int, price is a float
        # multiplying int x float gives a float result
        total_price = self.quantity * self.price    # float result
 
        # Round to 2 decimal places so it displays as a proper dollar amount
        total_price = round(total_price, 2)         # float, e.g. 240.00
 
        return total_price   # float
 
    # -------------------------------------------------------
    # def get_status - returns a str label based on stock level
    # Demonstrates: if / elif / else, int comparison
    # -------------------------------------------------------
    def get_status(self):
 
        # Compare quantity (int) to decide the stock status string (str)
        if self.quantity == 0:          # int compared to int 0
            status = "Out of Stock"     # str
        elif self.quantity < 50:        # int compared to int 50
            status = "Low Stock"        # str
        else:
            status = "In Stock"         # str
 
        return status   # str
 
    # -------------------------------------------------------
    # def check_available - returns True or False (bool)
    # based on whether the item passed validation
    # Demonstrates: if / else, True, False
    # -------------------------------------------------------
    def check_available(self):
 
        if self.is_valid == True:
            return True     # bool - item is valid and available
        else:
            return False    # bool - item failed validation
 
    # -------------------------------------------------------
    # def get_summary - returns a list of strings describing
    # this item's details
    # Demonstrates: for loop, continue, str conversion
    # -------------------------------------------------------
    def get_summary(self):
 
        # Each inner list holds a str label and its value
        # Values can be str, int, or float depending on the field
        fields = [
            ["Name",       self.name],              # str
            ["Quantity",   self.quantity],           # int
            ["Price ($)",  self.price],              # float
            ["Total ($)",  self.calculate_total()],  # float
            ["Status",     self.get_status()],       # str
        ]
 
        summary = []    # empty list to collect result lines (str)
 
        for field in fields:
            label = field[0]    # str - column heading
            value = field[1]    # str / int / float depending on field
 
            # Skip any field that has no value (empty string or None)
            if value == "" or value == None:
                continue    # move to the next field without adding this one
 
            # Convert value to str so it can be joined with the label string
            line = "  " + str(label) + ": " + str(value)   # str
            summary.append(line)
 
        return summary  # list of str lines