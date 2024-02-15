number1 = int(input("First #: ")) 
number2 = int(input("Second #: ")) 

def factors(num):
     factorlist = []
     for i in range(1, num+1): 
        if num%i==0: 
             factorlist.append(i) 
             return factorlist

factors1 = factors(number1)
factors2 = factors(number2)

for i in factors1[::-1]:
     if i in factors2:
        print(i)
        break


