# 6th task
print("\nმეექვსე დავალება")

combinedList = [1, 2, "George", "32", 32, "64", 128]
listOfInts = [item for item in combinedList if isinstance(item, int)]
listOfStrings = [item for item in combinedList if isinstance(item, str)]
print(listOfInts)
print(listOfStrings)
