number1 = int(input("First #: ")) 
number2 = int(input("Second #: ")) 

def factors(gcf):
     factorlist = []
     for i in range(1, gcf+1): 
        if gcf%i==0: # if it can leave no remainder 
             factorlist.append(i)  #adds to the end of the list
     return factorlist # outputs factorlist

# keeps adding one until it finds a factor and if it finds a factor it goes again

factors1 = factors(number1) # makes factors1 the factors of number1
factors2 = factors(number2) # makes factors2 the factors of number2

for i in factors1[::-1]: # loops through factors1 backwards
  if i in factors2: # if the factor is in factors2
    print(i) # print the factor
    break # only prints the greatest common factor and not the others

