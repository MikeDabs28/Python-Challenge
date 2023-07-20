#import modules that need to be utilized
import os
import csv

#locate the path to the csv data
budget_data = os.path.join('Resources', 'budget_data.csv')

#create text file to export to
text_file = "Analysis/Pybank_analysis.txt"

#set up lists and revenue parameters

months = 0
profit_total = 0
profit_change = 0
profit_start = 0

profit = []
monthly_changes = []
date = []

#open the csv data with the csv reader and indicate header row
with open(budget_data, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #indicate dataset has a header row
    csv_header = next(csvreader)
    first = next(csvreader)
    profit_start = int(first[1])

    for row in csvreader:
        #months start at 0 and add 1 to month count per each row of data is csvreader
        months = months + 1
        #store data for later use in calculations for increase/decrease
        date.append(row[0])
        #store the profit data and calculates the total profit
        profit.append(row[1])
        profit_total = profit_total + int(row[1])


        #average change in profits from month to month ; then calculate the average change in profits
        profit_end = int(row[1])
        profit_monthly = profit_end - profit_start
        #monthly changes will be added to the list to average out
        monthly_changes.append(profit_monthly)

        profit_change = profit_change + profit_monthly
        profit_start = profit_end

        #average change in profits
    average_profit_change =(sum(monthly_changes)/months)

    #using the monthly changes data, use functions max/min to locate the greatest increase and decrease. 
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    great_increase_date = date[monthly_changes.index(greatest_increase_profits)]
    great_decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${profit_total} \n"
    f"Average Change: ${average_profit_change}\n"
    f"Greatest Increase in Profits: {great_increase_date} ${greatest_increase_profits}  \n"
    f"Greatest Decrease in Profits: {great_decrease_date} ${greatest_decrease_profits}\n")

print(output)
       #print to external text
with open(text_file, "w") as txt_file:
    txt_file.write(output)