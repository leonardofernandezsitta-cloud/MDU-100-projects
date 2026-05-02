#!/usr/bin/env bash

echo "Enter the first number: "
read a
echo "Enter the second number: "
read b
echo "Enter a third number: "
read c

sum=$((a + b + c))
average=$(((a + b + c)/3))
product=$(((a * b * c)))

echo "The sum of the 3 numbers is: $sum"
echo "The average of the 3 numbers is: $average"
echo "The product of the 3 numbers is: $product"

