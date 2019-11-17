import json

with open('simple_test_json.txt','r') as f:
    print(json.load(f))