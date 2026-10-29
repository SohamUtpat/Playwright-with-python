#Assignment A: Create and read a list 

print("-------------------------------- Assignment A: Create and read a list --------------------------------")

test_cases = [
    "Login with valid username and password",
    "Login with invalid username and valid password",
    "Login with valid username and invalid password",
    "Login with invalid username and invalidpassword"
    ]

print(test_cases)
print(test_cases[0])
print(test_cases[-1])
print(len(test_cases))

#Assignment B: Add, remove and search operations 

print("-------------------------------- Assignment B: Add, remove and search operations --------------------------------")

modules = ["Login", "Search"]

modules.append("checkout")
print(modules)

modules.insert(1, "Profile")
print(modules)

modules.remove("Search")
print(modules)

print("Login" in modules)

#Assignment C: Slice and iterate 

print("-------------------------------- Assignment C: Slice and iterate --------------------------------")

modules = ["Pass", "Fail", "Pass", "Pass","Fail"]

print(modules[:3])
print(modules[2:])
for i in range(len(modules)):
    print(f"{i} -> {modules[i]}")

#Assignment D: list + tuples 

print("-------------------------------- Assignment D: list + tuples --------------------------------")

tuples = ("101", "Login valid user", "pass")

print(tuples[0])
print(tuples[1])
print(tuples[2])

test_data = [
    (201, "Login valid","pass"),
    (202, "Login invalid","fail"),
    (203, "Logout","pass"),
]

passed = 0
failed = 0

for i in range(len(test_data)):
    print(test_data[i])
    if test_data[i][2] == "pass":
        passed += 1
    else:
        failed += 1
print(f"passed: {passed} | failed: {failed}")    