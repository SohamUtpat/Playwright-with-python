#Assignment A: Arithmetic operations

print("-------------------------------- Assignment A: Arithmetic operations --------------------------------") 

Total_test_cases = 8
Total_passed = 6
Total_failed = Total_test_cases - Total_passed
Pass_rate = (Total_passed / Total_test_cases) * 100

print(f"Total test cases: {Total_test_cases}")
print(f"Total passed test cases: {Total_passed}")
print(f"Total_failed test cases: {Total_failed}")
print(f"Pass rate in percentage: {Pass_rate}")

print(f"Addition of passed and failed test cases: {Total_passed + Total_failed}")
print(f"substraction of total test cases and total failed: {Total_test_cases - Total_failed}")
print(f"multiplication of passed and failed test cases: {Total_passed * Total_failed}")
print(f"modulus of total test cases and total passed test cases: {Total_test_cases % Total_passed}")
print(f"Floor division of Total test cases and total passed test cases: {Total_test_cases // Total_passed}")

#Assignment B: Comparison operations

print("-------------------------------- Assignment B: Comparison operations --------------------------------")

expected_result = "pass"
actual_result = "fail"
expected_execution_time = 2.0
actual_execution_time = 3.0

print(f"Expected result is equal to actual result: {expected_result == actual_result}")
print(f"Actual result is not equal to expected result: {actual_result != expected_result}")
print(f"Actual duration time is greater than Expected duration time: {actual_execution_time > expected_execution_time}")
print(f"Actual duration time is greater than or equal to expected execution time: {actual_execution_time >= expected_execution_time}")

#Assignment C: Logical operations

print("-------------------------------- Assignment C: Logical operations --------------------------------")

username_valid = True
password_valid = False
login_successful = False

print(f"Username and Password are valid: {username_valid and password_valid}")
print(f"Username or Password are valid: {username_valid or password_valid}")
print(f"login successful not: {not login_successful}")


print("-------------------------------- Assignment D --------------------------------")

#Test case 1

name = "Login with valid username and password"
actual_result = "pass"
expected_result = "pass"
duration = 2.5
max_duration = 3.0

is_pass = actual_result == expected_result and duration <= max_duration
print(f"Test case 1: {name} is passed: {is_pass}")
#Test case 2

name = "Login with invalid username and valid password"
actual_result = "fail"
expected_result = "pass"
duration = 2.0
max_duration = 3.0

is_pass = actual_result == expected_result and duration <= max_duration
print(f"Test case 1: {name} is passed: {is_pass}")

#Test case 3

name = "Login with valid username and password"
actual_result = "pass"
expected_result = "pass"
duration = 4.0
max_duration = 3.0

is_pass = actual_result == expected_result and duration <= max_duration
print(f"Test case 1: {name} is passed: {is_pass}")

print("-------------------------------- Assignment E --------------------------------")

#Question 1 answer -- The difference between = and == is that = is used to assign the value to variable and == is used to compare the value of the variable

#Question 2 answer -- for the and opertaion the both conditions must be true to get the result true

#Question 3 answer -- not true give result false 

