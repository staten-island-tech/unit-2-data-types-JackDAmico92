

x = float(input('How much was the bill'))
j = "Your total was:"
tip = 0
gr = "a high"
g = "an above average"
b = "a low"
o = "a normal"
print("How was the service?")
service = input("service was:")
if service == "bad":
     print(f"You were billed for ${x}!")
     print("Your tip percentage is:")
     print("0%")
     tip = int(x*0)
     print(j)
     print(tip+x)
     print(f"You gave {b} tip!")
elif service == "okay":
     print(f"You were billed for ${x}!")
     print("Your tip percentage is:")
     print("15%")
     tip = int(x*0.15)
     print(j)
     print(tip+x)
     print(f"You gave {o} tip!")
elif service == "good":
     print(f"You were billed for ${x}!")
     print("Your tip percentage is:")
     print("20%")
     tip = int(x*0.20)
     print(j)
     print(tip+x)
     print(f"You gave {g} tip!")
elif service == "great":
     print(f"You were billed for ${x}!")
     print("Your tip percentage is:")
     print("25%")
     tip = int(x*0.25)
     print(j)
     print(tip+x)
     print(f"You gave {gr} tip!")

