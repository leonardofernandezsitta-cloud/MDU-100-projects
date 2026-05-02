#!usr/bin/env python3
# Project #2: Command-line Greeting

first = input("Enter your first name: ")
last = input("Enter your last name: ")
stu_ID = input("Enter your student ID: ")
full_name = first + ' ' + last + '. '
message = "Welcome to MDU " + full_name + " " + "(ID: " + stu_ID + "). " "You are now registered for Computer Science 101!"

print(message)
