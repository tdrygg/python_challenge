# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:45:34 2019

@author: tdryg
"""
# Import modules
import csv
import os

# Create path to csv
csvpath = os.path.join('budget_data.csv')

# Initialize variables for budget analysis
total_months = 0
total_revenue = 0
value = 0
change = 0
dates = []
profits = []

# Read csv
with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter= ',')
    
    # Read the header
    header = next(data)

    # Read the first row
    first_row = next(data)
    total_months += 1
    total_revenue += int(first_row[1])
    value = int(first_row[1])

    for row in data:
        
        # Append date to dates list
        dates.append(row[0])

        # Calculate change in revenue and append to profits list
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        # Add month to total_months
        total_months += 1

        # Add revenue to total_revenue
        total_revenue += int(row[1])

    # Calculate average change in profits/losses
    avg_change = round(sum(profits)/len(profits), 2)

    # Identify greatest increase in profits
    greatest_increase = max(profits)
    increase_index = profits.index(greatest_increase)
    greatest_increase_date = dates[increase_index]

    # Identify greatest decrease in profits
    greatest_decrease = min(profits)
    decrease_index = profits.index(greatest_decrease)
    greatest_decrease_date = dates[decrease_index]

# Financial Analysis
results = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Print results to terminal
print(results)

# Export results to text file
export_path = os.path.join('Financial_Analysis.txt')
with open(export_path, 'w') as txt_file:
    txt_file.write(results)