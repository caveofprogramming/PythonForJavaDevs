funcs = []

for i in range(5):
    funcs.append(lambda i=i: print(i))

for f in funcs:
    f()