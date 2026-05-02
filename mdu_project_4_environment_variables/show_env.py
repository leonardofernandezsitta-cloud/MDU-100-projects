#!/usr/bin/env python3

"""
Project #4: Environment Variables Reader (Python)
Demonstrates reading environment variables using os.environ.get()
"""

import os

print("=== Environment Variable Reader ===")
print("Enter a variable name to see it's value.")
print("(Example: HOME, PATH, USER, or your own exported variable)")
print()

var_name = input("Variable name: ")
value = os.environ.get(var_name, "NOT SET (variable does not exist or is not exported)")

print(f"\n{var_name} = {value}")
print("\nSecurity note: Use 'ps auxe' to see why environment variables are not secure for secrets.")
