from loader import load_json
from validator import validate_test_record

print("-------------------------------- Day 15: Test-data validator mini-project --------------------------------")

#Assignment A: Load data via loader module

print("-------------------------------- Assignment A: Load data via loader module --------------------------------")

data = load_json("sample_data.json")
print(f"tests loaded: {len(data['tests'])}")

#Assignment B: Validate each record

print("-------------------------------- Assignment B: Validate each record --------------------------------")

valid_count = 0
invalid_count = 0

for test in data["tests"]:
    ok, reason = validate_test_record(test)
    if ok == True:
        print(f"[{test['id']}] {test['name']} --> OK")
        valid_count += 1
    else:
        print(f"[{test['id']}] {test['name']} --> INVALID: {reason}")
        invalid_count += 1

#Assignment C: Summary report

print("-------------------------------- Assignment C: Summary report --------------------------------")

total = len(data["tests"])
print(f"total: {total} | valid: {valid_count} | invalid: {invalid_count}")

#Assignment D: Bad file handling

print("-------------------------------- Assignment D: Bad file handling --------------------------------")

missing = load_json("missing_sample_data.json")
print(missing)

print("Day 15 mini-project done")
