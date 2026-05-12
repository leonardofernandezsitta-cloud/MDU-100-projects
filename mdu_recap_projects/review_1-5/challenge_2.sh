#!/usr/bin/env bash

# Challenge 2: Secure To-Do List with Permissions
# This script creates a to-do list file, sets secure permissions (600),
# allows users to add tasks until typing 'done', and displays the final list.

# Print a visual separator and header to show the script has started
echo "===== Creating to do list... ====="

# Prompt the user for the name of their to-do list
# The -p flag allows us to display a prompt before reading input
read -p "Enter your to do list's name: " list_name

# Clean the filename by replacing any spaces with underscores
# ${list_name// /_} replaces ALL spaces with underscores
# Then we add .txt extension to make it clearly a text file
filename="${list_name// /_}.txt"

# Check if a file with this name already exists
# -f tests if the file exists and is a regular file
if [ -f "${filename}" ]; then
    # File exists - ask user if they want to overwrite it
    read -p "${filename} already exists. Overwrite? (y/n): " overwrite
    
    # Check if user answered 'n' (no)
    if [ "${overwrite}" = "n" ]; then
        # User chose NOT to overwrite - exit without making changes
        echo "===== No changes made to ${filename} ====="
        exit 0
    # Check if user answered 'y' (yes)
    elif [ "${overwrite}" = "y" ]; then
        # User wants to overwrite - create/empty the file
        # The > operator empties the file if it exists, or creates it if it doesn't
        > "$filename"
    fi
else
    # File does NOT exist - create a new empty file
    # The > operator creates the file
    > "$filename"
fi

# Set secure permissions on the file to 600
# 600 means: owner can read and write (6), group has no access (0), others have no access (0)
# This makes the to-do list private to the current user only
chmod 600 "${filename}"

# Start an infinite loop to collect tasks from the user
while true; do
    # Prompt user for a task
    # The prompt reminds them how to finish
    read -p "Enter new task (type 'done' to finish): " task
    
    # Check if the user typed 'done' (case-sensitive)
    if [ "$task" = "done" ]; then
        # User is finished - show confirmation message
        echo "===== Changes saved to $filename ====="
        # Break out of the while loop to stop asking for more tasks
        break
    fi
    
    # User entered a real task - append it to the file
    # The >> operator appends (adds to the end) without overwriting existing content
    echo "$task" >> "$filename"
done

# Display the contents of the to-do list with line numbers
# nl (number lines) adds line numbers to the output, making it easier to read
nl "${filename}"

# Explicitly exit with success code (0 means success, non-zero means error)
exit 0

