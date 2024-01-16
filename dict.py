dict = { "name" : "Sourav", "age" : 20}
print(dict["name"])
dict["clg"] = "GGM"
print(dict)
del dict["age"]
print(dict)

for key, value in dict.items():
	print(f"{key} : {value}")
