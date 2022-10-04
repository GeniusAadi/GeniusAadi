#Options for user
print('Use operators: +,-,x,/')
#start of the programme
for i in range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    a = float(input("Enter a number: "))
    b = input("Enter an operator: ")
    c = float(input("Enter another number: "))
#conditions for doing calculations
    while(True):
        if b == "+":
            print(a+c)
        elif b == "-":
            print(a-c)
        elif b == "x":
            print(a*c)
        elif b == "/":
            print(a/c)  
        else:
            print("Please enter a valid operator!")
        break      