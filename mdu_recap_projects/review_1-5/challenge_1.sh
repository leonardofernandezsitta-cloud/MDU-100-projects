# 1.- Shebang!
#!/usr/bin/env bash
# This script checks for existing environment variables and uses them or creates them to append a greeting line to a .txt file

# 2.- Use -z flag to check if environment variable ${USER_NAME} is empty:
if [ -z "${USER_NAME}" ]; then
	read -p "Enter you name(e.g.John Doe): " name
	export USER_NAME=${name}
else
	name=${USER_NAME}
fi
	
# 3.- Use -z flag to check if environment variable ${GREETING_FILE} is empty:
if [ -z "${GREETING_FILE}" ]; then
	filename="greeting_sh.txt"
	export GREETING_FILE=${filename}
else
	filename=${GREETING_FILE}
fi
	
# 4.- Set a variable for date: 
current_date=$(date "+%Y-%m-%d %H:%M:%S")

# 5.- Append a greeting string to "filename":
echo "Hello ${name}, today is ${current_date}. Have a good one!" >> ${filename}

# 6.- Display the last 3 lines of the file (tail command):
echo "===== Last 3 lines of ${filename} ====="
tail -3 ${filename}
