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
