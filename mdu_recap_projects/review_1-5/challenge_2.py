'''
====================================================================
====================================================================
============== Python Pseudo-Code for challenge 2 ==================
====================================================================
====================================================================
'''


# 1.- Shebang!:
#!/usr/bin/env python3
# This script creates a file with the name provided by the user, adds tasks, ends file when user types done + Enter
	
# 2.- Import os and sys:
import os
import sys
	
# 3.- Creates a to-do list file with name from user input (spaces → underscores) 
print("===== Creating your to do list... =====")
filename = input("Enter your list's name: ")
filename = filename.replace(" ", "_") + ".txt"
if os.path.exists(filename):
	yes_no = input(f"{filename} already exists, do you want to overwrite {filename}(y/n)? ")
	if yes_no == "y":
		with open(filename, 'w') as f:
			pass	# Pass creates empty files. When passing on f.write() we make sure the file is empty
	elif yes_no == "n":
		print(f"No changes made to {filename}.")
		sys.exit(0)
	else:
		print("Invalid input. Please enter 'y' or 'n'.")
		sys.exit(1)
else:
	# File does NOT exist - must be created (with open(filename, 'w') as f:)
	with open(filename, 'w') as f:
		pass 

# 4.- Sets permissions of that file to 600 (owner read/write only) using os.chmod(0o) 600:
os.chmod(filename, 0o600)

# 5.- Appends tasks until user types done:
while True:
	task = input(f"Enter a task or type done to save list to {filename}: ")
	if task == "done":
		break
	else:
		with open(filename, 'a') as f:
			f.write(task + "\n")
		
# 6.- Displays the file contents with line enumeration:
print(f"======= Your to do list: {filename} =======")
with open(filename, 'r') as f:
	lines = f.readlines()
	for i, line in enumerate(lines, start=1):
		print(f"{i}. {line.strip()}")

# 7.- Exit the program:
sys.exit(0)
	
