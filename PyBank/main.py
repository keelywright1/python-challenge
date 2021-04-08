import os
import csv

csv_path = os.path.join("..", "Resources", "PyBank", "budget_data.csv")
output_path = os.path.join("..", "Analysis", "PyBank_Analysis.txt")

with open(csv_path) as csv_file:
    csv_read = csv.reader(csv_file)

    next(csv_read) 

    months = 0
    total = 0
    total_ch = 0
    prev_rev = 0 
    inc = [0,'']
    dec = [0,'']
    

    for i, row in enumerate(csv_read):
        
        months += 1
        rev = int(row[1])
        total += rev
        change = rev - prev_rev
        prev_rev = rev

        if i == 0:
            change = 0
        total_ch += change

        # Greatest Increase in Profits
        if change > inc[0]:
            inc[0] = change
            inc[1] = row[0]
       
        # Greatest Decrease in Profits
        if change < dec[0]:
            dec[0] = change
            dec[1] = row[0]

    output = (
    f'\n    Financial Analysis\n\
    ----------------------------\n\
    Total Months: {months}\n\
    Total: ${total:,}\n\
    Average  Change: ${total_ch/(months-1):,.2f}\n\
    Greatest Increase in Profits: {inc[1]} (${inc[0]:,})\n\
    Greatest Decrease in Profits: {dec[1]} (${dec[0]:,})\n'
    )

open(output_path,'w').write(output)
print(output)