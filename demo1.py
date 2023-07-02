sum = 0
while(True):
    userInput = input("Enter the price: \n")
    if userInput != 'q':
        sum = sum + int(userInput)
        print(f"Your bill so far {sum}")
    else:
        print(f"your bill total is {sum}. Thanks for shopping with us")
        break