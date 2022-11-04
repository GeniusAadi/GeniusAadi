#Making a CUI calculator
#Options for user
print('Use operators: +,-,x,/')
#start of the programme
while True:
    a = float(input("Enter a number: "))
    b = input("Enter an operator: ")
    c = float(input("Enter another number: "))
#conditions for doing calculations
    if b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "x":
        print(a*c)
    elif b == "/":
        print(a/c)  
    else:
        print("Error : Enter a valid operator!")
