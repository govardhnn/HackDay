from random import *
def flipacoin():
    print("-----------Going to flip a coin------------------")
    choice=input("Enter your choice - (HEADS/TAILS)")
    flag=randint(0,1)
    F=-1
    if choice=='HEADS':
        F=1
    elif choice=='TAILS':
        F=0
    else:
        print('invalid input')
    if flag==F:
        print('You won!')
    else:
        print("Better luck next time")
flipacoin()

    

        
    
