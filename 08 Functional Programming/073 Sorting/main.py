animals1 = ("dog", "giraffe", "elephant", "tiger", "lion")

animals2 = sorted(animals1, reverse=True, key=lambda s: len(s))

print(animals2)