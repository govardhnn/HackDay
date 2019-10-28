from random import *
num=int(input("Enter the number of flips-(odd number)\t"))
i=0
j=0
if(num==0):
    print("Invalid input: input must be >0 and odd")
elif(num%2==1):
    while(num>0):
        val=randint(0,1)
        if(val%2==0):
            print("\nHEADS")
            i+=1
        else:
            print("\nTAILS")
            j+=1
        num-=1

    if(j>i):
        print("\nTAILS WINS")
    else:
        print("\nHEADS WINS")
else:
    print("Enter an odd number only")

    

        
    