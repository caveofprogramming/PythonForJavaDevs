
value = 7

try:
    assert value > 8, "Oh no!"
except AssertionError as a:
    print(a)