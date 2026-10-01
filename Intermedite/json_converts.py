import json

data = '{"name":"rahul","age":23}'
print(type(data))

result = json.loads(data)
print(type(result))
print(result['name'])
