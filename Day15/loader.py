import json

def load_json(filepath):
    try:
        file = open(filepath, "r")
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("file not found")
        return None
    except json.JSONDecodeError:
        print("invalid JSON file")
        return None
