import re

tag = r'<div id="123">Hello</div>'

result = re.match(
    r"""
        <div\s+     # Match opening tag
        id="(\d+)"  # Match ID
        >           # Closing tag bracket
        ([^<>]+)    # Get content between open and close tags.
        </div>
    """, 
    tag, re.VERBOSE)

print("No match" if result is None else result.groups())