'''c=1
i=int(input("Last line"))
while(c<=i):
    print("*"*c)
    c+=1'''
#print(str(True))
#from math import *
#print(sqrt(-22))
from random import *
#help(random)
'''a=[1,2,3,4,5]
l=a
seed(2)
i=10
while(i>0):
    print(a)
    if(a==l):
        print("Jinxx")
    shuffle(a)
    i=i-1'''


while(True):
    a=randint(100,200);
    if(a%2==0):
        print(a,chr(a),sep=" ")
    else:
        print("New set \n")
        continue
    if(a==150):
        break
    
    
    
