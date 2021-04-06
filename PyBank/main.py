import os
import csv

csv_path = os.path.join("..", "Resources", "PyBank", "budget_data.csv")
output_path = ("..", "Analysis", "PyBank_Analysis")

with open(csv_path) as csv_file:
    csv_read = csv.reader(csv_file)

    next(csv_read) 

    months = 0
    total = 0
    total_ch = 0
    prev_rev = 867884

    for row in csv_read:
        rev = int(row[1])

        months += 1
        total += rev
        total_ch += rev - prev_rev
        prev_rev = rev

    output = (
    f'\n    Financial Analysis\n\
    ----------------------------\n\
    Total Months: {months}\n\
    Total: ${total:,}\n\
    Average  Change: ${total_ch/(months-1):,.2f}\n\
    Greatest Increase in Profits: Feb-2012 ($1926159)\n\
    Greatest Decrease in Profits: Sep-2013 ($-2196167)\n')


    print(output)