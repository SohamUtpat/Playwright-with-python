import json

#Assignment A: Basic try / except

print("-------------------------------- Assignment A: Basic try / except --------------------------------")

try:
    number = int("abc")
    print(number)
except ValueError:
    print("invalid number, cannot convert to int")

#Assignment B: Read text file with try / except

print("-------------------------------- Assignment B: Read text file with try / except --------------------------------")

try:
    file = open("test_data.txt", "r")
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    print("test_data.txt not found")

#Assignment C: Handle missing file

print("-------------------------------- Assignment C: Handle missing file --------------------------------")

try:
    file = open("missing_file.txt", "r")
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    print("file is missing, cannot read test data")

#Assignment D: Read JSON test data and handle invalid JSON

print("-------------------------------- Assignment D: Read JSON test data and handle invalid JSON --------------------------------")

try:
    file = open("test_data.json", "r")
    data = json.load(file)
    file.close()
    print(data)

    for test in data["tests"]:
        print(f"{test['id']} --> {test['name']} --> {test['status']}")

except FileNotFoundError:
    print("test_data.json not found")
except json.JSONDecodeError:
    print("invalid JSON file")

try:
    bad_json = "{id: 1, name: broken}"
    data = json.loads(bad_json)
    print(data)
except json.JSONDecodeError:
    print("invalid JSON string, cannot load test data")
