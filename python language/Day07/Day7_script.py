#Assignment A: Create and read a dictionary

print("-------------------------------- Assignment A: Create and read a dictionary --------------------------------")

user = {
    "username": "sohamqa",
    "role": "QA Engineer",
    "email": "soham@test.com",
    "active": True
}

print(user)
print(user["username"])
print(user["role"])
print(user.get("email"))

#Assignment B: Add, update and remove dictionary keys

print("-------------------------------- Assignment B: Add, update and remove dictionary keys --------------------------------")

test_case = {
    "id": 101,
    "name": "Login valid user",
    "status": "pass"
}

print(test_case)

test_case["duration"] = 1.5
print(test_case)

test_case["status"] = "fail"
print(test_case)

del test_case["duration"]
print(test_case)

print("name" in test_case)

#Assignment C: Loop through dictionary / test data

print("-------------------------------- Assignment C: Loop through dictionary / test data --------------------------------")

test_data = {
    "tc01": "pass",
    "tc02": "fail",
    "tc03": "pass",
    "tc04": "pass"
}

for key in test_data:
    print(f"{key} --> {test_data[key]}")

passed = 0
failed = 0

for status in test_data.values():
    if status == "pass":
        passed += 1
    else:
        failed += 1

print(f"passed: {passed} | failed: {failed}")

#Assignment D: Sets and remove duplicate usernames

print("-------------------------------- Assignment D: Sets and remove duplicate usernames --------------------------------")

usernames = ["sohamqa", "admin", "sohamqa", "guest", "admin", "tester"]

print(usernames)

unique_usernames = set(usernames)
print(unique_usernames)

unique_list = list(unique_usernames)
print(unique_list)
print(f"original count: {len(usernames)} | unique count: {len(unique_list)}")
