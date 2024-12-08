days = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thur": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday",
}

del days["Mon"]

print(days)

print(days.pop("Thur"))
print(days)

print(days.popitem())
print(days)

days.clear()
days = {}
print(days)