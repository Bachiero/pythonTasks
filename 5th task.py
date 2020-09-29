# 5th task
print("\nმეხუთე დავალება")

while True:
    try:
        firstNumber = int(input("დაწერეთ პირველი რიცხვი: "))
        secondNumber = int(input("დაწერეთ მეორე რიცხვი: "))
        break
    except ValueError:
        print("Please enter the number")
print(firstNumber * secondNumber)