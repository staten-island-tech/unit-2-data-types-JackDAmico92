print('2 numbers needed to find GCF')

x = int(input('Number#1: '))
y = int(input('Number#2: '))
def factors(num):
 factorlist = []
 for i in range(1,num+1):
  if num%i == 0:
   print('The GCF is: ')
   print(int(i))
  