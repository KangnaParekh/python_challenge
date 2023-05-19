#import library
import os
import csv

#path to collect data from the Resources folder
budget_data=os.path.join('Resources','budget_data.csv')
print (budget_data)

#adjust variables
P = []
months = []
total_months=0
greatest_increase=["",9999999]
greatest_decrease=["",0]
revenue_change=[]
revenue_average=0

#open and read csv file
with open(budget_data,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next (csvfile)


    #skip header row
    print(f"Header:{csv_header}")

    #find net amount of profit and loss
    #read through each row of data after skipping header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    #find revenue change
    for x in range(1,len(P)):
        revenue_change.append((int(P[x])-int(P[x-1])))

    #calculate average revenue change
    revenue_average=sum(revenue_change)/len(revenue_change)

    #calculate total length of months
    total_months +=1

    #calculate increase and decrease in revenue
    greatest_increase=max(revenue_change)
    greatest_decrease=min(revenue_change)

#print the results in parent file
print("Financial Analysis")
print("........................................................................")
print("Total Months:" + str(total_months))
print("Total:" +"$" +str(revenue_average))
print ("Greatest Increase in Profits:" + str(months[revenue_change.index(max(revenue_change))+1])+"" + "$" + str(greatest_increase))
print("Greatest Increase in Profits:" + str(months[revenue_change.index(min(revenue_change))+1])+"" + "$" + str(greatest_decrease))

#print the output to a text file
file=open("output.txt","w")
file.write("Financial Analysis" + "\n")

file.write("...................................................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(P)) + "\n")

file.write("Average change: " + "$" + str(revenue_average) + "\n")

file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

file.close()
