SAMPLE_USERS = [
    {"username": "sohamqa", "password": "test123"},
    {"username": "admin", "password": "admin123"},
    {"username": "guest", "password": "123"},
]

TEST_CASES = [
    (101, "Login valid user", "pass"),
    (102, "Login invalid password", "fail"),
    (103, "Logout", "pass"),
]
