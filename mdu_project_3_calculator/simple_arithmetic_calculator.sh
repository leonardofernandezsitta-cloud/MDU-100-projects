#!/usr/bin/env bash
echo "Enter bill amount: $"
read bill
echo "Enter tip percentage: "
read tip_percent
echo "Enter number of people: "
read people

# bc does the math. scale=2 means 2 decimal places
tip_amount=$(echo "scale=2; $bill * $tip_percent / 100" | bc)
total_with_tip=$(echo "scale=2; $bill + $tip_amount" | bc)
per_person=$(echo "scale=2; $total_with_tip / $people" | bc)

echo ""
echo "Bill: \$$bill"
echo "Tip ($tip_percent%): \$$tip_amount"
echo "Total with tip: \$$total_with_tip"
echo "Each person pays: \$$per_person"

# I just coppied your code because I want to understand everything before writing my own .sh
