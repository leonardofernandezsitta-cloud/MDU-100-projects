# 100 Projects: From Zero to Engineer

**Author:** Leonardo Fernandez Sitta (noobian1)  
**Goal:** Master programming, computer science, mathematics, cybersecurity, and systems engineering through 100 progressively complex projects.

## Repository Structure

| Folder | Project | Concepts |
|--------|---------|----------|
| `mdu_project_1_hello_world/` | Hello World | Terminal, ASCII, system calls |
| `mdu_project_2_greeting/` | Greeting | User input, variables, string concatenation |
| `mdu_project_3_calculator/` | Calculator | Integers, floats, division, bc, f-strings |
| `mdu_project_4_environment_variables/` | Environment Variables | export, ps auxe, security |
| `mdu_project_5_file_io/` | File I/O | read/write/append, file modes, `with open` |
| `mdu_recap_projects/review_1_5/` | Review 1-5 | Three challenges combining Projects 1-5 |

More projects will be added as I progress.

## Technologies Used

- **Python 3** (primary for learning)
- **Bash** (terminal automation and scripting)
- JavaScript and C++ will be added in later phases

## How to Run Any Project

1. Clone this repository:
   ```bash
   git clone https://github.com/leonardofernandezsitta-cloud/MDU-100-projects.git
   cd MDU-100-projects

    Navigate to a project folder:
    bash

    cd mdu_project_X_project_name/

    Run Python version:
    bash

    python3 filename.py

    Run Bash version:
    bash

    chmod +x filename.sh
    ./filename.sh

Progress Tracker
#	Project	Status	Key Learning
1	Hello World	✅	Terminal, ASCII, system calls
2	Greeting	✅	User input, variables, string concatenation
3	Calculator	✅	int/float, division, bc, f-strings
4	Environment Variables	✅	export, ps auxe, security
5	File I/O	✅	File modes, append vs write, with open
Review	Challenges 1-5	✅	Environment-aware greeting, secure to-do list, permission probability
6-100	...	🔴	In progress
What I Learned So Far

Programming Concepts:

    Variables, data types, user input, and output in Python and Bash

    String concatenation and f-string formatting

    Type conversion (int(), float(), str())

    Conditional statements (if/elif/else) and loops (while, for)

    Functions and methods

File I/O:

    Reading, writing, and appending to files

    File modes: 'r', 'w', 'a'

    with open() for automatic file closing

Environment & System:

    Shell vs environment variables (difference and inheritance)

    export for making variables available to child processes

    ps auxe reveals environment variables → insecure for secrets

Security & Permissions:

    File permissions: 600 (owner read/write only), 755 (owner all, group/others read+execute)

    chmod for changing permissions

    Why environment variables are not secure for passwords or API keys

Mathematics:

    Counting combinations (e.g., environment variable names)

    Probability calculations (1/8 for owner digit, 1/512 for exact permission)

    Octal to rwx conversion

Terminal & Git:

    Basic commands: cd, ls, pwd, nano, cat, chmod

    Git workflow: add, commit, push

    GitHub for version control and portfolio

License

MIT — free for learning purposes.
Disclaimer

All code is for educational use. No real secrets or passwords are stored here.
