# Project 2: Command-Line Greeting

## Problem
At a school registration desk, staff need to print personalized welcome messages for each student. Doing this by hand is slow and error-prone.

## Solution
Write a program that asks for first name, last name, and student ID, then prints a custom greeting.

## Code Files

| File | Description |
|------|-------------|
| `greet.py` | Python version |
| `greet.sh` | Bash version |

## What I Learned

- `input()` returns a string in Python
- `read` reads user input in Bash
- String concatenation with `+` in Python
- Variables in Bash use `$` to expand
- Single quotes `'` vs double quotes `"` in Bash

## How to Run

**Python:**
```bash
python3 greet.py

Bash:
bash

chmod +x greet.sh
./greet.sh

Sample Output
text

Enter your first name: Alice
Enter your last name: Cooper
Enter your student ID: 00123
Welcome to MDU Alice Cooper (ID: 00123)! You are now registered for Computer Science 101!

Key Takeaway

Always convert user input to the correct type (int, float) before doing math.
