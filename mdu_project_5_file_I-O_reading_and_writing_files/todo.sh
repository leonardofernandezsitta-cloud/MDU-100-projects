#!/usr/bin/env bash
# Takes user input, creates user_chosen_name.txt, appends input to user_chosen_name.txt, prints a list

echo "Please enter your list's name: "
read list_name
filename="${list_name// /_}.txt"
echo "$list_name" > "$filename"



while true; do
	echo  "Insert new task (or type done + enter to finish): "
	read  task
	if [ "$task" = "done" ]; then
		break
	fi
	echo "$task" >> "$filename"
done 

echo "Your list is saved as: $filename"
cat "$filename"

