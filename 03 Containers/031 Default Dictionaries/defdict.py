from collections import defaultdict

people = {
    "Bob": 42,
    "Sue": 53,
    "Steve": 25,
}

print(people.get("Ethel", 99))

days = defaultdict(str)

days.update({"Mon": "Monday", "Tue": "Tuesday"})

print(days["Wed"])