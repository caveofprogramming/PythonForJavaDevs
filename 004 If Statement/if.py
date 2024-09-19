# and, not, or
# True, False

raining = False
temperature = 18

if temperature > 19 and not raining:
    print("Weather fine")
elif not raining:
    print("At least it's dry")
else:
    print("Stay indoors")

mood = "good" if not raining else "bad"
print(mood)