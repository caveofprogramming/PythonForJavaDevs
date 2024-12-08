import re

menu = """
1. Fish
2. Bread
3. Peppers
4. Potatoes
"""

result = re.findall(r"(\d+)\.\s+(\w+)\n", menu)

print(result)