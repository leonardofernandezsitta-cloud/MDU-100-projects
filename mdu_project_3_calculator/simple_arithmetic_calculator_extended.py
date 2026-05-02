#!/usr/bin/env python3
# This is the extended version with separated calculation for tip and bill and printing all info for the user

bill = float(input("Enter your bill amount(00.00): "))
tip = int(input("Enter the tip amount: " "%"))
people = int(input("Enter the number of people you will split the bill in: "))
bill_split = bill / people
tip_amt = (bill * tip)/100
tip_split = ((bill * tip)/100)/people
total_bill = bill +  (bill * tip)/100
total_bill_split = total_bill / 4

if people <= 0:
	print("Error: Number of people less than 1.") 
else: 
	print(f'Your bill is {bill}.')
	print(f'Your bill of {bill} devided by {people} is: {bill_split}.')
	print(f'The {tip}% tip of your bill of {bill} is: {tip_amt}.')
	print(f'Your tip devided by {people} is: {tip_split}.')
	print(f'Your total bill with tip included is: {total_bill}.')
	print(f'Your total bill with tip included devided by {people} is: {total_bill_split}.')
