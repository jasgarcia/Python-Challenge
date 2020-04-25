#add dependencies
import os
import csv


#load csv file create the star for output
csvfile = os.path.join("Resources", "budget_data.csv")
outputcsv = os.path.join("Results", "Bank.txt")

with open(csvfile, newline='') as csvdata:
    datareader = csv.reader(csvdata, delimiter=',')
    print(datareader)
    csv_header = next(datareader)
    months = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               

#Months       
    for row in datareader:
        months.append(row[0])
        revenue.append(row[1])
    print(len(months))
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = months[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = months[j+1]

#Print Statements
 

print("----------------------------------------------------------")

print(f'Financial Analysis'+'\n')

print("----------------------------------------------------------")

print("Total number of months: " + str(len(months)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

print("----------------------------------------------------------")

text_file = open(outputcsv,"w")