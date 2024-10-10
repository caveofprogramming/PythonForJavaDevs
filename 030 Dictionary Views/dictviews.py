people = {
    "Bob": 42,
    "Sue": 53,
    "Steve": 25,
}

keys = people.keys()
values = people.values()
items = people.items()

print(type(keys))
print(type(values))
print(type(items))

item_list = list(items)
print(items)
del people["Steve"]
print(items)
print(item_list)