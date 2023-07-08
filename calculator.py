#Making a calculator
#option for user
print("Please enter any from given operators: (+,-,x,/)")
while True:
  try:
    a = float(input("Please enter your first number = " ))
    c = float(input("Please enter your second number = "))
    b = (input("Please enter your operator = " ))
#conditions for calculation
    if b == "+":
      print(a + c)
    elif b == "-":
      print(a - c)
    elif b == "x":
      print(a * c)              
    elif b == "/":
      print(a / c)
    else:
      print("Error : Please enter a valid operator!")  
#for showing error if a and c are not numbers
  except ZeroDivisionError:
    print("Error : Please enter a non-zero number!")
  except Exception as e:
    print("Error : Please enter a number!")                
