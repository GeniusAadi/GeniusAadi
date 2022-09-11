import random
l="roll"
while l == "roll":
    random_number=random.randint(1,6)
  #  dice=("1","2","3","4","5","6")
    if random_number == 1:
        print("┌--------------┐")
        print("│              │")
        print("│       0      │")
        print("│              │")
        print("└--------------┘")
    elif random_number == 2:
         print("┌--------------┐")
         print("│0             │")
         print("│              │")
         print("│            0 │")
         print("└--------------┘")
    elif random_number == 3:
         print("┌--------------┐")
         print("│0             │")
         print("│      0       │")
         print("│            0 │")
         print("└--------------┘") 
    elif random_number == 4:
         print("┌--------------┐")
         print("│0           0 │")
         print("│              │")
         print("│0           0 │")
         print("└--------------┘")
    elif random_number == 5:
         print("┌--------------┐")
         print("│0           0 │")
         print("│       0      │")
         print("│0           0 │")
         print("└--------------┘")    
    elif random_number == 6:
         print("┌--------------┐")
         print("│0     0    0  │")
         print("│              │")
         print("│0     0    0  │")
         print("└--------------┘")
 #   choice = random.choice(dice)
  #  print(choice)  
    l=input("Type roll for another chance otherwise press any key to exit.")
    
    