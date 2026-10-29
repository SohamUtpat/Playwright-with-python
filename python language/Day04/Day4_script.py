#Assignment A: Basic If-else statement

print("-------------------------------- Assignment A: If-else statement --------------------------------")

actual_result = "pass"
expected_result = "pass"

if actual_result == expected_result:
    print("Test case is passed")
else:
    print("Test case is failed")

#Assignment B: If-else statement login 

print("-------------------------------- Assignment B: If-else statement login --------------------------------")

username = "sohamqa"
password = "test123"
entered_username = "sohamqa"
entered_password = "test123"

if entered_username == username and entered_password == password :
    print("login successful")
else:
    print("login failed")    


#Assignment C: If-elif-else statement

print("-------------------------------- Assignment C: If-elif-else statement --------------------------------")

password = "pass1234567382"
has_digit = True

if len(password) < 8:
    print("password is too small")

elif not has_digit:
    print("password must contain digit")

else:
    print("password looks valid")

#Assignment D: Login decision tree 

print("-------------------------------- Assignment D: Login decision tree --------------------------------")

username = "sohamQA"
password = "test123"
entered_username = "sohamQA"
entered_password = "test123"
account_locked = False

if entered_username == username and entered_password == password and not account_locked:
    print("Access granted")
elif entered_username == username and entered_password != password:
    print("Invalid password")
elif entered_username != username and entered_password == password:
    print("Invalid username")
elif account_locked:
    print("Locked message")
else:
    print("Access denied")          

#Assignment E: QNA

print("-------------------------------- Assignment E: QNA --------------------------------")

#Question 1 answer -- the elif run the second condition if the first condtion is false
#Question2 answer -- the else run the block when all the above conditions are false
#Question3 answer -- the order is important because if the account is locked in first condition then the valid or invalid username and password not matters 



