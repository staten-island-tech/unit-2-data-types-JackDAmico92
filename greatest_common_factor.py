print('2 numbers needed to find GCF')

x = int(input('Number#1: '))
y = int(input('Number#2: '))
z = 0
j = z+1
def gcf(x,y):
  if y%j == x%j:  
   print('the gcf is:')
   print(j)
gcf(x,y)