#Assignment A: __init__ basics

print("-------------------------------- Assignment A: __init__ basics --------------------------------")

class LoginData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

login1 = LoginData("sohamqa", "test123")
login2 = LoginData("admin", "admin123")

print(login1.username)
print(login2.username)

#Assignment B: TestCase class

print("-------------------------------- Assignment B: TestCase class --------------------------------")

class TestCase:
    def __init__(self, test_id, name, status):
        self.test_id = test_id
        self.name = name
        self.status = status

    def summary(self):
        return f"[{self.test_id}] {self.name} --> {self.status}"

tc1 = TestCase(101, "Login valid user", "pass")
tc2 = TestCase(102, "Login invalid password", "fail")
tc3 = TestCase(103, "Logout", "pass")

print(tc1.summary())
print(tc2.summary())
print(tc3.summary())

#Assignment C: Validation method

print("-------------------------------- Assignment C: Validation method --------------------------------")

class LoginData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid(self):
        if self.username == "":
            return False
        if len(self.password) < 6:
            return False
        return True

print(LoginData("sohamqa", "test123").is_valid())
print(LoginData("", "test123").is_valid())
print(LoginData("sohamqa", "123").is_valid())
print(LoginData("admin", "password").is_valid())

#Assignment D: Count pass/fail from objects

print("-------------------------------- Assignment D: Count pass/fail from objects --------------------------------")

tests = [
    TestCase(201, "Search product", "pass"),
    TestCase(202, "Add to cart", "fail"),
    TestCase(203, "Checkout", "pass"),
    TestCase(204, "Payment fail", "fail"),
]

passed = 0
failed = 0

for i in range(len(tests)):
    print(tests[i].summary())
    if tests[i].status == "pass":
        passed += 1
    else:
        failed += 1

print(f"passed: {passed} | failed: {failed}")
print("Day 13 classes and __init__ done")
