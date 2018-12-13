#PyBank Challenge

import os
import csv

budget_data_csv = os.path.join("..", "budget_data.csv")
months = []
total_PNL = 0
avg_PNL = 0
pnl_list = []
greatest_increase = 0
greatest_decrease = 0

with open(budget_data_csv, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        months.append(row[0])
        pnl_list.append(int(row[1]))

total_months = len(months)                           
total_PNL = (sum(pnl_list))
pnl_pairs = list(zip(pnl_list, pnl_list[1:]))
pnl_diffs = [x[1] - x[0] for x in pnl_pairs]
avg_pnl_change = round((sum(pnl_diffs) / (len(pnl_diffs))),2)
greatest_increase = (max(pnl_diffs))
greatest_decrease = (min(pnl_diffs))

max_month = months[pnl_diffs.index(max(pnl_diffs)) + 1]  
min_month = months[pnl_diffs.index(min(pnl_diffs)) + 1]  

print("                      ")
print("Financial Analysis")
print("--------------------")
print(f"Total months: {total_months}")
print(f"Total: {total_PNL}")
print(f"Average Change: {avg_pnl_change}")
print(f"Greatest Increase in Profits: {max_month} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {min_month} ({greatest_decrease})")
print("                      ")


