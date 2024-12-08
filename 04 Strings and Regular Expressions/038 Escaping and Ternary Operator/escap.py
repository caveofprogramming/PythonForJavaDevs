import re

text = r"a\nz"

result = re.match(r"a\\nz", text)

print("No match" if result is None else result.group())