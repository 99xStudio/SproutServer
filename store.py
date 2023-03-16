import json

def get(name):
    with open(name + ".json", "r") as f:
        return json.load(f)
    
def add(name, item):
    with open(name + ".json", "r") as f:
        arr = json.load(f)
    arr.append(item)
    with open(name + ".json", "w") as f:
        json.dump(arr, f)