#Assignment A: For loop

print("-------------------------------- Assignment A: For loop --------------------------------")

count = 1

for count in range(1,6):
    print(f"Running test case: {count}")

#Assignment B: for loop with list

print("-------------------------------- Assignment B: for loop with list --------------------------------")

results = ["pass", "fail","pass","pass","fail"]

passed = 0
failed = 0

for result in results:
    print(result)
    if result =="pass":
        passed += 1
    else:
        failed +=1

print(f"Total passed: {passed}")
print(f"Total failed: {failed}")

#Assignment C: While loop

print("-------------------------------- Assignment C: While loop --------------------------------")

attempt = 1

while attempt <= 3:
    print(f"Login attempt number: {attempt}")
    attempt +=1

#Assignment D: Process test cases 

print("-------------------------------- Assignment D: Process test cases --------------------------------")

tests = [
    "login valid user",
    "Login invalid password",
    "Logout",
]

statuses = ["Pass","Fail","Pass"]

passed = 0
failed = 0

for i in range(len(tests)):
    print(f"{tests[i]} --> {statuses[i]}")
    
    if statuses[i] == "Pass":
        passed += 1
    else:
        failed += 1

print(f"Total: {len(tests)} | Passed: {passed} | Failed: {failed}")            


