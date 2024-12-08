animals1 = ["Dog", "cat", "ELEPHANT", "Badger"]

animals2 = map(lambda s: s[:3].lower(), animals1)

print(list(animals2))