# 7th task
import math
print("\nმეშვიდე დავალება")

customInput = input("ჩაწერეთ ინფუთი და გამოყავით მძიმით, მაგ: 'ნიკა,იოგურტი, დევი, ხე':  ")

oneList = customInput.split(",")

print(oneList)

Len = len(oneList)
if Len %2 == 0:
    print("even")
else:
    print("odd")

middle = math.floor(Len / 2)
ifodd = middle - 1
if Len % 2 != 0:
    print(oneList[middle])
else:
    print(oneList[ifodd] + oneList[middle])

