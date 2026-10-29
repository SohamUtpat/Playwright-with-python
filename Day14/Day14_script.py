import json

#Assignment A: Load JSON file

print("-------------------------------- Assignment A: Load JSON file --------------------------------")

file = open("login_data.json", "r")
data = json.load(file)
file.close()
print(data)

#Assignment B: Iterate records

print("-------------------------------- Assignment B: Iterate records --------------------------------")

for login in data["logins"]:
    print(f"{login['username']} | password length: {len(login['password'])} | expected: {login['expected']}")

#Assignment C: Validate vs expected

print("-------------------------------- Assignment C: Validate vs expected --------------------------------")

for login in data["logins"]:
    username = login["username"]
    password = login["password"]
    expected = login["expected"]

    if username != "" and len(password) >= 6:
        result = "valid"
    else:
        result = "invalid"

    if result == expected:
        print(f"{username} --> {result} --> PASS")
    else:
        print(f"{username} --> {result} (expected {expected}) --> FAIL")

#Assignment D: Exception handling

print("-------------------------------- Assignment D: Exception handling --------------------------------")

try:
    file = open("missing_login_data.json", "r")
    data = json.load(file)
    file.close()
    print(data)
except FileNotFoundError:
    print("file is missing, cannot read login data")

try:
    bad_json = "{username: admin, password: 123}"
    data = json.loads(bad_json)
    print(data)
except json.JSONDecodeError:
    print("invalid JSON string, cannot load login data")

print("Day 14 JSON and test data done")
