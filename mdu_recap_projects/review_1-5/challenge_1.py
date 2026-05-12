#!/usr/bin/env python3
# This script uses environment variables to append a greeting to a text file and to read from the same text file

# 1. Import os and datetime modules

import os
import datetime


# 2. Check if USER_NAME exists in environment:
#       If yes, get its value and store in a variable called 'name'
#       If no or empty, ask user "Enter your name:" and store in 'name'
#       Then set os.environ['USER_NAME'] = name

if  not os.environ.get("USER_NAME"):
	name = input("Enter your name: ")
	os.environ["USER_NAME"] = name
else:
	name = os.environ.get("USER_NAME")
	
	
# 3. Check if GREETING_FILE exists in environment:
#       If yes, get its value and store in a variable called 'filename'
#       If no or empty, ask user "Enter filename:" and store in 'filename'
#       Then set os.environ['GREETING_FILE'] = filename

if os.environ.get("GREETING_FILE"):
	filename = os.environ.get("GREETING_FILE")
else:
	filename = input("Enter file name: ")
	os.environ["GREETING_FILE"] = filename

# 4. Create a timestamp using datetime.now()
#       Format it nicely (e.g., "2026-05-04 15:30:22")

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 5. Create the greeting string:
#       f"Hello {name}, it is {time_stamp}. Have a good one!\n"

greeting = f'Hello {name}, it is {time_stamp}. Have a good one!\n'


# 6. Open the file in append mode ('a') using the filename variable
#       Write the greeting string to the file

with open(filename, 'a') as f:
	f.write(greeting)
	
	
# 7. Open the same file in read mode ('r')
#       Read all lines into a list using .readlines()
#       Get the last 3 lines using slicing: last_lines = all_lines[-3:]

with open(filename, 'r') as f:
	all_lines = f.readlines()
	last_lines = all_lines[-3:]


# 8. Print a header like "=== Last 3 lines of [filename] ==="
#       Loop through last_lines and print each one

print(f"=== Last 3 lines of {filename} ===")

for line in last_lines:
	print(line.strip())   # .strip() removes the \n


# 9. (Optional) Print a confirmation message

print("Mission accomplished!")

