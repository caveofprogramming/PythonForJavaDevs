def catalogue(name, *args):

    print("Type: ", type(args))

    print(name)

    if len(args) >= 1:
        print(args[0])

    for value in args:
        print(value)

catalogue("Trees", "oak", "ash", "linden")
catalogue("Blank")