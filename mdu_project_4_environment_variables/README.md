# Project 4: Environment Variables and Secret Leakage

## Problem
A developer stores an API key in an environment variable, thinking it is secure. Another user on the same system runs `ps auxe` and sees the key in plain text.

## Solution
Demonstrate how environment variables work, how child processes inherit them, and why they are NOT secure for secrets.

## Code Files

| File | Description |
|------|-------------|
| `show_env.py` | Python script that reads any environment variable by name |
| `show_env.sh` | Bash script that does the same |
| `project_4_solutions.txt` | My notes, quiz answers, and math exercise |

## What I Learned

### Shell Variable vs Environment Variable

| Type | Command | Visible to child processes? |
|------|---------|----------------------------|
| Shell | `color=blue` | No |
| Environment | `export color=blue` | Yes |

### The Security Problem

```bash
export SECRET="test_1_2"
ps auxe | grep SECRET   # Shows the secret!

Any user on the system who can run ps auxe can see environment variables of running processes.
Reading Environment Variables in Code

Python:
python

import os
value = os.environ.get("VAR_NAME", "default_value")

Bash:
bash

value="${VAR_NAME:-default}"

Commands Learned
Command	Purpose
env	Show all environment variables
export VAR=value	Create an environment variable
unset VAR	Remove an environment variable
ps auxe	Show all processes with their environment
echo $VAR	Print a variable's value in Bash
How to Run
bash

export TEST_VAR="hello"
python3 show_env.py   # Enter: TEST_VAR
./show_env.sh         # Enter: TEST_VAR
ps auxe | grep TEST_VAR   # See the security issue

Sample Output
text

=== Environment Variable Reader ===
Enter a variable name to see its value.
(Example: HOME, PATH, USER, or your own exported variable)

Variable name: TEST_VAR

TEST_VAR = hello

Security note: Use 'ps auxe' to see why environment variables are not secure for secrets.

Key Takeaways

    Never store passwords, API keys, or real secrets in environment variables

    export is required for child processes to see a variable

    ps auxe reveals environment variables to any user on the system

    The proper way to store secrets is in files with restricted permissions

