import re

text = """
one
two
three
"""

result = re.search(r"(t.*e)", text, re.DOTALL)

print("No match" if result is None else result.groups())