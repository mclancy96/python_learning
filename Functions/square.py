def square(num):
    return num**2

number = 0
while True:
    print("Enter a number or type \"exit\" to leave")
    number = input()
    if number != "exit" and float(number):
        print(square(float(number)))
    elif number == "exit":
        break
    else:
        print("Not a number. Try again")