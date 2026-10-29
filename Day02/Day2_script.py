#Day02: Variables and Data Types and typecasting by Soham

#Assignments of Day02

#Create variables for one test case using different types:
Test_id = 100
Test_name = "Login with valid Username and Password"
duration = 3.6
Status = True

print("Test ID:", Test_id, type(Test_id))
print("Test Name:", Test_name, type(Test_name))
print("Duration in seconds:", duration, type(duration))
print("Status:", Status, type(Status))

#Assignnment B - Type conversion :

Test_id = "101"
execution_time = "2.5"
Status = ""

print("Test ID:",Test_id)
print("Execution Time:",execution_time)
print("Status:",Status)

Test_id = int(Test_id)
execution_time = float(execution_time)
Status = bool(Status)

print("Test ID:",Test_id)
print("Execution Time:",execution_time)
print("Status:",Status)

#Assignment C - f-strings:

Test_case_id = 150
Test_case_name = "Login with invalid username and valid password"
duration = 2.4
module = "Authenication"

print(f"Test case id: {Test_case_id} | Test case name: {Test_case_name} | execution time in seconds : {duration} | covered module: {module}")

#Assignment D - Test-case summary printer:
#Testcase1
Test_case_id = 201
Test_case_name = "Login with valid Username and Password"
status = "Pass"
Duration = 1.5
print(f"TC-{Test_case_id} | {Test_case_name} | {status} | {Duration}s")

#Testcase2
Test_case_id = 202
Test_case_name = "Login with invalid Username and valid Password"
status = "Pass"
Duration = 1.7
print(f"TC-{Test_case_id} | {Test_case_name} | {status} | {Duration}s")

#Testcase3
Test_case_id = 203
Test_case_name = "Login with valid Username and invalid Password"
status = "Fail"
Duration = 1.9
print(f"TC-{Test_case_id} | {Test_case_name} | {status} | {Duration}s")

# Summary totals
total = 3
passed = 2
failed = 1
pass_rate = (passed / total) * 100
print(f"Total: {total} | Passed: {passed} | Failed: {failed} | Pass rate: {pass_rate:.2f}%")

#Assignment E - self-check
"""
1.Difference between = and ==?
2.Why is 2 different from "2"?
3.What does an f-string do? """

"""
1. The single '=' is the assign operator which is used to assign the values to variables and
   "==" is the comparison operator which is used to compare the values.
2. The difference in 2 and "2" is the two without double quotes is integer value and
   two with diuble quotes is string value.
3. An f-string allows to insert variables and expressions directly into a text message.   
"""

