# figure out a way to simplify tip calc/ put prints and stuff behind the if statement- leading to less lines of code
print('How much was the bill?')
x = float(input('The bill was: '))
j = "Your total was:"
long = print("Your tip percentage is: ")
tip = 0
gr = "a high"
g = "an above average"
b = "a low"
o = "a normal"
print("How was the service?")
service = input("service was: ")
if service == "bad":
     print(f"You were billed for ${x}!")
     long
     print("0%")
     tip = int(x*0)
     print(j)
     print(tip+x)
     print(f"You gave {b} tip!")
elif service == "okay":
     print(f"You were billed for ${x}!")
     long
     print("15%")
     tip = int(x*0.15)
     print(j)
     print(tip+x)
     print(f"You gave {o} tip!")
elif service == "good":
     print(f"You were billed for ${x}!")
     long
     print("20%")
     tip = int(x*0.20)
     print(j)
     print(tip+x)
     print(f"You gave {g} tip!")
elif service == "great":
     print(f"You were billed for ${x}!")
     long
     print("25%")
     tip = int(x*0.25)
     print(j)
     print(tip+x)
     print(f"You gave {gr} tip!")

