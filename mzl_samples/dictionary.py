# key - value pair collection

#initalize
info = {
    "name" : "MZL",
    "address" : "Ygn",
    "score" : [1,2,3,4,5]
}

#upsert - update insert
info["Job"] = "SSS"

print(info)

#delete
info.pop("Job")
#delete last
info.popitem()
print(info)

print()

#loop (key default)
for item in info:
    print(item)
    print(info[item]) #indexer

print()

#loop through values
for value in info.values():
    print(value)

#loop throuth key and value pair
for key,value in info.items():
    print(f"Key : {key}, value : {value}")