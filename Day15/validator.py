def is_empty(text):
    if text == "":
        return True
    else:
        return False

def password_ok(password, min_length=6):
    if len(password) >= min_length:
        return True
    else:
        return False

def validate_login(username, password):
    if is_empty(username):
        return False
    if is_empty(password):
        return False
    if password_ok(password) == False:
        return False
    return True

def validate_test_record(record):
    required = ["id", "name", "username", "password", "status"]

    for key in required:
        if key not in record:
            return False, f"missing key: {key}"

    if record["status"] != "pass" and record["status"] != "fail":
        return False, "status must be pass or fail"

    if validate_login(record["username"], record["password"]) == False:
        if is_empty(record["username"]):
            return False, "empty username"
        if is_empty(record["password"]):
            return False, "empty password"
        if password_ok(record["password"]) == False:
            return False, "password too short"
        return False, "invalid login data"

    return True, "ok"
