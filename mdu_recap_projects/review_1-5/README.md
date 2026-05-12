# Review 1-5: Foundational Projects Recap

This folder contains my solutions to three review challenges that consolidate everything learned in Projects 1-5.

## Challenges Overview

| Challenge | Description | Python | Bash |
|-----------|-------------|--------|------|
| 1 | Environment-Aware Greeting | ✅ | ✅ |
| 2 | Secure To-Do List with Permissions | ✅ | ✅ |
| 3 | Permission Probability Calculator | ✅ | ✅ |

---

## Challenge 1: Environment-Aware Greeting

**Goal:** Read environment variables (`USER_NAME`, `GREETING_FILE`), fall back to user input if not set, append a timestamped greeting to a file, and display the last 3 lines.

**Key concepts:**
- Environment variables with `os.environ` (Python) and `export` (Bash)
- User input fallback with `input()` and `read -p`
- File appending with `'a'` mode (Python) and `>>` (Bash)
- Timestamp generation with `datetime` (Python) and `date` (Bash)
- Display last 3 lines with slicing `[-3:]` (Python) and `tail -3` (Bash)

**Files:**
- `challenge_1.py` - Python implementation
- `challenge_1.sh` - Bash implementation

---

## Challenge 2: Secure To-Do List with Permissions

**Goal:** Create a to-do list file with user-provided name, set permissions to 600 (owner read/write only), append tasks until user types "done", and display contents with line numbers. If file exists, ask to overwrite.

**Key concepts:**
- Filename sanitization (spaces → underscores)
- File existence check with `os.path.exists()` (Python) and `[ -f ]` (Bash)
- File modes: `'w'` (write/overwrite) and `'a'` (append)
- Permission setting with `os.chmod(filename, 0o600)` and `chmod 600`
- Loop with `while True` and `break` on "done"
- Display with line numbers using `enumerate()` (Python) and `nl` (Bash)

**Files:**
- `challenge_2.py` - Python implementation
- `challenge_2.sh` - Bash implementation

---

## Challenge 3: Permission Probability Calculator

**Goal:** Accept a 3-digit octal permission (each digit 0-7), validate input, convert to rwx string using a dictionary mapping, and calculate probability of random owner permission match.

**Key concepts:**
- Input validation (length and digit range)
- Associative array/dictionary for octal → rwx mapping
- String slicing to extract individual digits
- Probability calculation: 1/8 = 12.5% (owner digit has 8 possible values)
- Arithmetic with `bc` in Bash for decimal percentage

**Files:**
- `challenge_3.py` - Python implementation
- `challenge_3.sh` - Bash implementation

---

## Math Bootcamp

The `math_bootcamp.txt` file contains solutions to mathematical problems related to:
- Counting possible environment variable names (combinations with constraints)
- Converting octal permissions to rwx strings and vice versa
- Calculating total permission combinations (8³ = 512)
- Probability of specific permission matches (1/8 for owner digit, 1/512 for exact permission)

---

## How to Run

### Python scripts
```bash
python3 challenge_1.py
python3 challenge_2.py
python3 challenge_3.py

