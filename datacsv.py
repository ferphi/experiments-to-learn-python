import csv
import string
numbers=string.digits
number_of_columns=0
# Create CSV file for test
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['A', 'B', 'C', 'D'])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([5, 6, 7, 8])
    writer.writerow([9, 10, 11, 12])
#counting number of columns in CSV file   
with open('data.csv', 'r') as csvfile:
    reader=csv.reader(csvfile, delimiter=",")
    for row in reader:
        number_of_columns+=1
#validation
while True:
    #entry instructions
    print("\nEnter the columns to sum, separated by , ")
    print("for example: 1,2,3")
    #Ask the user for the columns to sum
    columns=input("\nEnter the columns to sum: ")
    columns=columns.strip()
    columns=columns.split(",")
    if all(x in numbers for x in columns) and len(columns)<=number_of_columns:
        if all(int(x)<=number_of_columns for x in columns):
            break
        else:
            print("\nYour entry is not valid, please try again.")
    else:
        print("\nYour entry is not valid, please try again.")                               
#Read CSV file and calculate sum of selected columns
with open('data.csv', 'r') as csvfile:
    reader=csv.reader(csvfile)
    next(reader)  # Skip the first row containing the headers
    total=[0]*len(columns)
    for row in reader:
        for i in range(len(columns)):
            total[i]+=int(row[int(columns[i])-1])
#Write the result of the sum to another file
with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["The sum of the selected columns respectively is: "])
    writer.writerow(total)
print("The sum of the selected columns respectively is: ", total)
