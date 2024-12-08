class MyException(Exception):
    pass

try:
    raise MyException("Oh no!")
except MyException as e:
    print(e)