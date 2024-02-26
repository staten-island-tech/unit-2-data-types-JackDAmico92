number1 = int(input("First #: ")) 
number2 = int(input("Second #: ")) 

def factors(num):
     factorlist = []
     for i in range(1, num+1): 
        if num%i==0: 
             factorlist.append(i) 
     return factorlist


