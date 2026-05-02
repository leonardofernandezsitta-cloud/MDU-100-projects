# Project 3: Simple Arithmetic Calculator

## Problem
You and friends go to a restaurant. The bill is $47.50. You want to add 15% tip and split among 4 people. Manual math is error-prone.

## Solution
Write a program that asks for bill amount, tip percentage, and number of people, then calculates the per-person cost.

## Code Files

| File | Description |
|------|-------------|
| `simple_arithmetic_calculator.py` | Basic Python version |
| `simple_arithmetic_calculator_extended.py` | Python version with error handling |
| `simple_arithmetic_calculator.sh` | Bash version using `bc` |

## What I Learned

- `int()` converts to whole numbers (people count)
- `float()` converts to decimal numbers (money)
- f-string formatting: `f"{value:.2f}"` shows 2 decimal places
- Python division `/` always returns a float
- Bash needs `bc` for decimal math
- Error handling: checking if `people <= 0`

## How to Run

**Python:**
```bash
python3 simple_arithmetic_calculator_extended.py

Bash:
bash

chmod +x simple_arithmetic_calculator.sh
./simple_arithmetic_calculator.sh

Sample Output
text

Enter your bill amount(00.00): 47.50
Enter the tip amount: %15
Enter the number of people you will split the bill in: 4
Your bill is 47.5.
Your bill of 47.5 devided by 4 is: 11.875.
The 15% tip of your bill of 47.5 is: 7.125.
Your tip devided by 4 is: 1.78125.
Your total bill with tip included is: 54.625.
Your total bill with tip included devided by 4 is: 13.65625.

Key Takeaway

Always validate user input. Division by zero crashes programs.
