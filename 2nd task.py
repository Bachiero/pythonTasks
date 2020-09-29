# 2nd task
print("\nმეორე დავალება")
MyNumbers = [1, 11, 23, 44, 54, 76, 9, 76, 32, 4, 565, 87, 545]

# ჩემი ამოხსნა
# luwi = [i for i in MyNumbers if not int(i)%2]
# kenti = [i for i in MyNumbers if int(i)%2]
#
# print(luwi)
# print(kenti)

# ციკლით ამოხსნა
evenNumbers = []
oddNumbers = []
for i in MyNumbers:
    if int(i) % 2 == 0:
        evenNumbers.append(i)
print(evenNumbers)

for j in range(len(MyNumbers)):
    if int(j) % 2 != 0:
        oddNumbers.append(j)
print(oddNumbers)