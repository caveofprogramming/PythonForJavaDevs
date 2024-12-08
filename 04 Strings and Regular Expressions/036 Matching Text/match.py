import re

text = "Once upon a time"

result = re.match(r"o.*?time", text, flags=re.IGNORECASE)

if result is None:
    print("No match")
else:
    print(result.group())