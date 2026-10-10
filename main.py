import random

print(f"This is your random number: {random.randint(1,100)}\n")

min=1
max=100

AIguess= random.randint(min,max)
print(f"Is your number {AIguess}?")

while True:
    UserInput = int(input("Choose a number from: 1.too low  2.too high  3.correct\n"))

    if UserInput == 1:
        min=AIguess
    elif UserInput == 2:
        max=AIguess
    elif UserInput ==3:
        print("Guess successful")
        break

    AIguess=(min+max)//2
    print(f"Is your number {AIguess}\n")