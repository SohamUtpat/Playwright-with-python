def is_empty(text):
    if text == "":
        return True
    else:
        return False

def format_result(test_id, test_name, status):
    return f"[{test_id}] {test_name} --> {status}"

def validate_login(username, password):
    if username == "" or password == "":
        return False
    if len(password) < 6:
        return False
    return True
