#!/usr/bin/env bash
# Project #4: Environment Variable Reader (Bash)
# Demonstrates reading environment variables using ${!var_name}

echo "=== Environment Variable Reader ==="
echo "Enter a variable name to see its value."
echo "(Example: HOME, PATH, USER, or your own exported variable)"
echo ""

read -p "Variable name: " var_name

# ${!var_name} is indirect expansion: it uses the value of var_name as a variable name
value="${!var_name:-NOT SET (variable does not exist or is not exported)}"

echo ""
echo "${var_name} = ${value}"
echo ""
echo "Security note: Run 'ps auxe | grep ${var_name}' to see why environment variables are not secure for secrets."


