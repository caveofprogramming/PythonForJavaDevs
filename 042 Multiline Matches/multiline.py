import re

menu = """
1. Fish
2. Bread
3. Peppers
4. Potatoes
"""

result = re.findall(r"^(.*)$", menu, re.MULTILINE)

print(result)