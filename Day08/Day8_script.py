#Assignment A: Basic function

print("-------------------------------- Assignment A: Basic function --------------------------------")

def greet():
    print("Hello from Day 08 functions")

greet()

#Assignment B: Function with arguments (login data validation)

print("-------------------------------- Assignment B: Function with arguments (login data validation) --------------------------------")

def validate_login(username, password):
    if username == "" or password == "":
        return False
    if len(password) < 6:
        return False
    return True

print(validate_login("sohamqa", "test123"))
print(validate_login("", "test123"))
print(validate_login("sohamqa", "123"))
print(validate_login("admin", "password"))

#Assignment C: String check functions

print("-------------------------------- Assignment C: String check functions --------------------------------")

def is_empty(text):
    if text == "":
        return True
    else:
        return False

def starts_with_login(text):
    if text.startswith("Login"):
        return True
    else:
        return False

print(is_empty(""))
print(is_empty("pass"))
print(starts_with_login("Login valid user"))
print(starts_with_login("Logout"))

#Assignment D: Format test result

print("-------------------------------- Assignment D: Format test result --------------------------------")

def format_result(test_id, test_name, status):
    return f"[{test_id}] {test_name} --> {status}"

print(format_result(101, "Login valid user", "pass"))
print(format_result(102, "Login invalid password", "fail"))
print(format_result(103, "Logout", "pass"))

results = [
    (201, "Search product", "pass"),
    (202, "Add to cart", "fail"),
    (203, "Checkout", "pass"),
]

for i in range(len(results)):
    test_id = results[i][0]
    test_name = results[i][1]
    status = results[i][2]
    print(format_result(test_id, test_name, status))
