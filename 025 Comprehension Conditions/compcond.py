words1 = ["it", "was", "the", "best", "of", "times"]

words2 = [w for w in words1 if len(w) > 3]
print(words2)

words3 = [w.upper() if len(w) > 3 else w for w in words1]
print(words3)