months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(months["Jan"])

months["Apr"] = "April"

print(months)

months.update({"May": "May", "Jun": "June"})
print(months)

for month in months:
    print(month, months[month])

for month in months.keys():
    print(month, months[month])

for month in months.values():
    print(month)

for abbrev, name in months.items():
    print(abbrev, name)

print("Oct" in months)