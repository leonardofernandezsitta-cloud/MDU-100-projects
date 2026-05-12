# 1.- Program Set Up:

#!/usr/bin/env python3

import sys

# 2.- Data Set Up:

octal_dict = {
	0 : "---",
	1 : "--x",
	2 : "-w-", 
	3 : "-wx", 
	4 : "r--", 
	5 : "r-x", 
	6 : "rw-", 
	7 : "rwx"
	}
	
oct_val_lst=[]
for i in range(0, 8):
	oct_val_lst.append(str(i))
	
# 3.- Get octal permission from user:

usr_input=list(input("Enter an octal permission (e.g. 750): "))

# 4.- Validate/Show user input:

while True:
	if len(usr_input) != 3:
		usr_input=list(input("Octal permission has to be no more or less than 3 digits from 0 to 7, try again: "))
		continue
	if usr_input[0] not in oct_val_lst: 
		usr_input=list(input("Octal permission has to be no more or less than 3 digits from 0 to 7, try again: "))
		continue
	if usr_input[1] not in oct_val_lst:
		usr_input=list(input("Octal permission has to be no more or less than 3 digits from 0 to 7, try again: "))
		continue
	if usr_input[2] not in oct_val_lst:
		usr_input=list(input("Octal permission has to be no more or less than 3 digits from 0 to 7, try again: "))
		continue
	else:
		print("\n")
		break


# 5.- Print results from user input

while True:    
	if len(usr_input) == 3:
		print(f'The length of octal permission "{usr_input}" is "{len(usr_input)}".\n')
		break
	if usr_input[0] in oct_val_lst:
		owner=usr_input[0]
		print(f'Owner permission "{owner}" is valid and found in range "{oct_val_lst}".\n')
		break
	if usr_input[1] in oct_val_lst:
		user=usr_input[1]
		print(f'User permission "{user}" is valid and found in range "{oct_val_lst}".\n')
		break
	if usr_input[2] in oct_val_lst:
		others=usr_input[2]
		print(f'Others permission "{others}" is valid and found in range "{oct_val_lst}".\n')
	else:
		continue

# 6.- Convert input into "rwx" string.

owner=usr_input[0]
user=usr_input[1]
others=usr_input[2]
rwx = octal_dict[int(owner)] + octal_dict[int(user)] + octal_dict[int(others)]

print(f'Your "rwx" permission is: {rwx}.\n')

# 7.- Calculate the probability that a randomly set permission would have the same owner permissions (first digit)

# x = amount of possible octal numbers to choose (0-7 = 8)
# y = 1 because out of all 8 digits for owner permissions only 1 can be used
x = 8
y = 1
probability = f'{y/x*100}% or {y}/{x} (one over eight).'
print(f'The probability of user permission being randomly picked the same as user input is: {probability}\n') 

print(f'Owner permission is: {owner}')
print(f'User permission is: {user}')
print(f'Others permission is: {others}')
print(f'User entered permission: {owner}{user}{others} = {rwx}')

sys.exit(0)
