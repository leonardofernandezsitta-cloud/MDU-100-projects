#!/usr/bin/env python3
# This program creates a to do list (user_chosen_name.txt), asks for items to add to the list and shows the list's name and content.


listname = input("Please enter your list's name: ")
filename = listname.replace(" ", "_") + ".txt"
with open(filename, 'w') as f:
	f.write(listname + "\n" + "\n")

while True:
	task = input("Insert new task (or type 'done + Enter' to finish): ")
	if task == "done":
		break
	with open(filename, 'a') as f:
		f.write(task + "\n")

print(f'Your list has been saved as: {listname}')
print("=== Your list content ===")
with open(filename, 'r') as f:
	print(f.read())	



