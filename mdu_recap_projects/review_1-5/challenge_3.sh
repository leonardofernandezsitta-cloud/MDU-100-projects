#!/usr/bin/env bash

# 1.- Declare an associative array
declare -A octal_dict

# Add key-value pairs
octal_dict[0]="---"
octal_dict[1]="--x"
octal_dict[2]="-w-"
octal_dict[3]="-wx"
octal_dict[4]="r--"
octal_dict[5]="r-x"
octal_dict[6]="rw-"
octal_dict[7]="rwx"

# Get user input octal permission and turn string to an array
read -p "Enter an octal permission (e.g. 642): " usr_input
echo $usr_input
octal_array=($(echo "$usr_input" | fold -w1))

echo "Array length: ${#octal_array[@]}"
echo "First element: ${octal_array[0]}"
echo "All elements: ${octal_array[@]}"

# Validate user input length
length=${#usr_input}
echo $length
if [ $length -ne 3 ]; then
    echo "Error: octal permission have to be 3 digits."
    exit 1
else
    echo "The length of your octal permission is $length."
fi

# Set a valid numbers string
allowed="01234567"

# Set variables for verification
owner="${usr_input:0:1}"
user="${usr_input:1:1}"
others="${usr_input:2:1}"

if [[ $allowed == *"$owner"* && $allowed == *"$user"* && $allowed == *"$others"* ]]; then
    echo "Owner permission $owner is allowed."
    echo "User permission $user is allowed."
    echo "Others permission $others is allowed."
else
    echo "Error: octal permissions may only be digits 0-7."
    exit 1
fi

# Convert to rwx string (e.g., rw-r-----)
rwx="${octal_dict[$owner]}${octal_dict[$user]}${octal_dict[$others]}"
echo "$rwx"

# Calculate the probability that a randomly set permission would have the same owner permissions (first digit)
# x is the amount of permission 0-7 = 8
x=8
# y represents owner permission posibilities = 1
y=1
probability=$(echo "scale=2; $y*100 / $x" | bc)
echo "Owner permission $owner has a probability of $probability or $y/$x."
