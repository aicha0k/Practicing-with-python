print("welcome to python pizza delivery")
size = input("what size pizza do you want? S, M, or L\n")
add_pepperoni = input("would you like pepperoni? Y or N\n")
add_cheese = input("would you like extra cheese? Y or N\n")
total = 0
if size == "S":
    total = total + 15
    if add_pepperoni == "Y":
        total = total + 2
    if add_cheese == "Y":
        total = total + 1    
elif size == "M":
    total = total + 20
    if add_pepperoni == "Y":
        total = total + 3
    if add_cheese == "Y":
        total = total + 1
elif size == "L":
    total = total + 25
    if add_pepperoni == "Y":
        total = total + 3
    if add_cheese == "Y":
        total = total + 1

print("the total is $",total)


