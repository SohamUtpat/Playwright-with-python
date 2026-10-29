import math
from datetime import date

from test_data import SAMPLE_USERS, TEST_CASES
from helpers import is_empty, format_result, validate_login

#Assignment A: Built-in modules

print("-------------------------------- Assignment A: Built-in modules --------------------------------")

print(math.sqrt(16))
print(math.pi)
print(f"today: {date.today()}")

#Assignment B: Import test_data module

print("-------------------------------- Assignment B: Import test_data module --------------------------------")

print(SAMPLE_USERS)
for i in range(len(SAMPLE_USERS)):
    user = SAMPLE_USERS[i]
    print(f"{user['username']} | password length: {len(user['password'])}")

print(TEST_CASES)
for i in range(len(TEST_CASES)):
    print(f"{TEST_CASES[i][0]} --> {TEST_CASES[i][1]} --> {TEST_CASES[i][2]}")

#Assignment C: Import helpers module

print("-------------------------------- Assignment C: Import helpers module --------------------------------")

print(is_empty(""))
print(is_empty("pass"))
print(format_result(101, "Login valid user", "pass"))
print(format_result(102, "Login invalid password", "fail"))
print(validate_login("sohamqa", "test123"))
print(validate_login("", "test123"))
print(validate_login("sohamqa", "123"))

#Assignment D: venv + pip note

print("-------------------------------- Assignment D: venv + pip (terminal practice) --------------------------------")

print("venv created in project folder: .venv")
print("activate: .venv\\Scripts\\activate")
print("installed with pip: requests")

try:
    import requests
    print(f"requests version: {requests.__version__}")
except ImportError:
    print("requests not in this Python - run with: .venv\\Scripts\\python.exe Day11_script.py")

print("Day 11 modules practice done")