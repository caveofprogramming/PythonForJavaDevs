import re

text = "dog cat mouse"

regex = re.compile(r"C.*T", flags=re.IGNORECASE)

result = re.sub(regex, "giraffe", text)

print(result)