'''
Day 2: Lists, dictionaries, sets, tuples and JSON
'''
#Lists
ai_models = ["GPT", "Claude", "Gemini", "Llama"]

# Accessing list elements
print("------------------------------- Lists -------------------------------------------")
print(ai_models[0])
print(ai_models[-1])

# Add items to list or push items to the list
ai_models.append("Mistral")
ai_models.remove(ai_models[2])

print("Total number of models:", len(ai_models))
# Iterating over a list : use for loop
for model in ai_models:
    print(model)
    
    
# Dictionaries
ai_model_dict = {
    "name": "GPT",
    "version": 6,
    "active": True,
    "cost": 2.50
}

# Accessing dictionary values
print("------------------------------- Dictionaries -------------------------------------------")
print(ai_model_dict["name"])
print(ai_model_dict["version"])

# Updating dictionary values
ai_model_dict["active"] = False

# Adding a new key-value pair
ai_model_dict["provider"] = "OpenAI"

# Removing a key-value pair
ai_model_dict.pop("cost")

print(ai_model_dict)
print("total number of dictionary entries: ", len(ai_model_dict))

# Dictionary items()
for key, value in ai_model_dict.items():
    print(key, value)
    

# Sets
print("------------------------------- Sets -------------------------------------------")
ai_models_set = {"GPT", "Claude", "Gemini"}
print(ai_models_set)

# Removing Duplicates
models = ["GPT", "Claude", "GPT", "Gemini", "Llama", "Claude", "Mistral"]
unique_models = set(models)

print("Unique models:", unique_models)
print("Total number of unique models:", len(unique_models))
unique_models.add("DeepSeek")
unique_models.discard("Llama")

if "GPT" in unique_models:
    print("GPT exists")

print("GPT" in unique_models)
# unique_models.add("GPT")
# print(unique_models)

for model in unique_models:
    print(model)
    
# unique_models.remove("Llama")
# print(unique_models)

# tuple
models_tuple = ("GPT", "Claude", "Gemini", "GPT", "Llama")

print("------------------------------- tuple -------------------------------------------")
print(models_tuple[0])
print(models_tuple[-1])

# Slicing
print(models_tuple[1:4]) #The start index is included, and the stop index is excluded.

print(models_tuple.count("GPT"))
print(models_tuple.index("Gemini"))

print("Total number of element in tuple:", len(models_tuple))

for model in models_tuple:
    print(model)