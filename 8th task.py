# 8th task
print("\nმერვე დავალება\n")



while True:
    try:
        customInput = int(input("ჩაწერე რიცხვი: "))
        break
    except ValueError:
        print("Please enter the number")

newList = list(range(1, customInput))
myList = []

def myFunc():
    for item in newList:
        if item % 3 == 0 or item % 5 == 0:
            myList.append(item)
    return myList
myFunc()

print(myList)
print(sum(myList))
