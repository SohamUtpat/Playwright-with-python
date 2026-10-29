# Day 10 — Revision checkpoint 1
# Small CLI test-data utility (variables, conditions, loops, functions, exceptions)

print("-------------------------------- Day 10: CLI test-data utility --------------------------------")

test_cases = []

def add_test(test_id, name, status):
    test = {
        "id": test_id,
        "name": name,
        "status": status
    }
    test_cases.append(test)
    print(f"added: {test_id} - {name}")

def show_tests():
    if len(test_cases) == 0:
        print("no test cases yet")
    else:
        for i in range(len(test_cases)):
            t = test_cases[i]
            print(f"{t['id']} | {t['name']} | {t['status']}")

def count_results():
    passed = 0
    failed = 0
    for t in test_cases:
        if t["status"] == "pass":
            passed += 1
        elif t["status"] == "fail":
            failed += 1
    print(f"total: {len(test_cases)} | passed: {passed} | failed: {failed}")

def load_from_file(filename):
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if len(parts) != 3:
                print(f"skip invalid line: {line}")
                continue
            add_test(parts[0], parts[1], parts[2])
        print("file loaded")
    except FileNotFoundError:
        print("file not found")

# demo run (same ideas as menu, without waiting for input all night)
add_test("101", "Login valid user", "pass")
add_test("102", "Login invalid password", "fail")
add_test("103", "Logout", "pass")

print("-------------------------------- show tests --------------------------------")
show_tests()

print("-------------------------------- count results --------------------------------")
count_results()

print("-------------------------------- weak topics note --------------------------------")
# Variables: store values with names (id, name, status, lists, dicts)
# Conditions: if / elif / else decide pass vs fail / empty list
# Loops: for over list to print and count
# Functions: add_test, show_tests, count_results, load_from_file
# Exceptions: try/except FileNotFoundError when file missing
# Weak topics to revisit tonight: sets + file JSON + writing functions from blank

print("weak topics: sets, JSON files, writing functions from blank")
print("Day 10 revision utility done")
