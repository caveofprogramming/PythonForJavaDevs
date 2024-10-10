try:
    d = {}
    d['Hello']

    print(1/0)
except ZeroDivisionError as zde:
    print("Failed.", zde)
except Exception as e:
    print("Caught exception", type(e))
finally:
    print("Finally!")