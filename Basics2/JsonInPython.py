import json

ai_model = {
    "name": "GPT",
    "active": True,
    "code": 2.50
}

json_data = json.dumps(ai_model)

print(json_data)
print(type(json_data))

# Converting JSON to a Dictionary

python_data = json.loads(json_data)
print(python_data)
print(type(python_data))

#part A — Python Dictionary to JSON
ai_response = {
    "model": "GPT",
    "message": "Hello! How can I help you?",
    "tokens_used": 150,
    "success": True
}

json_ai_response = json.dumps(ai_response)
print(json_ai_response)
print(type(json_ai_response))

# part B JSON to Python Dictionary
python_ai_response = json.loads(json_ai_response)
print(python_ai_response)
print(type(python_ai_response))
print(python_ai_response["message"])
print(python_ai_response["tokens_used"])