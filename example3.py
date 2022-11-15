print("--------Welcome to the tip calculator--------")
total = float(input("what was the total bill? $"))
percentage = int(input("will the tip be of , 10, 12 or 15? "))
num = int(input("how many people will be splitting the bill? "))
percentage = 1 + percentage / 100
pay_per_person = (total / num) * percentage
print("each person should pay $",round(pay_per_person,2))
print("the total bill is $",round(total/num))
print("--------Thank you for using the tip calculator--------")

