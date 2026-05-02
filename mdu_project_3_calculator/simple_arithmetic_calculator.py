#!/usr/bin/env python3
# project#3: simple arithmetic calculator

bill = float(input("Enter your bill amount(00.00): "))
tip = int(input("Enter the tip amount you want to add to your bill(10, 15, 20, etc.): "))
float tip_amt = tip * bill / 100
float sum = bill + tip_amt
float split = sum / 4

print(split)
