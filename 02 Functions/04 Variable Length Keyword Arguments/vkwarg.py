def details(name, **kwargs):
    print("Name", name)

    print(type(kwargs))
    print(kwargs)

    if "height" in kwargs:
        print("Height", kwargs["height"])

    for key in kwargs:
        print(key, kwargs[key])

details("Sue", height=170, age=42)