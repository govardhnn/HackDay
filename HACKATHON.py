
from random import *
print("Welcome To The Game Of Snakes and Ladders")
print("Ready Player One And Two")
i=0

o1=o2=n1=n2=0
while(i==0):
        k=1
        while(k<=2):
            print("*************************")
            print("Player ",k,":")

            ch=input("Press Enter to Roll Dice")

            r=randint(1,6)
            print("The Dice Value is",r)
            if(k==1):
                k=2
                n1=r+o1
                if (n1 == 1):
                    n1 = 38
                    print("Ladder!")
                elif (n1 == 4):
                    n1 = 14
                    print("Ladder!")
                elif (n1 == 9):
                    n1 = 31
                    print("Ladder!")
                elif (n1 == 17):
                    n1 = 7
                    print("Snake!")
                elif (n1 == 21):
                    n1 = 42
                    print("Ladder!")
                elif (n1 == 28):
                    n1 = 84
                    print("Ladder!")
                elif (n1 == 51):
                    n1 = 67
                    print("Ladder!")
                elif (n1 == 54):
                    n1 = 34
                    print("Snake!")
                elif (n1 == 62):
                    n1 = 19
                    print("Snake!")
                elif (n1 == 64):
                    n1 = 60
                    print("Snake!")
                elif (n1 == 72):
                    n1 = 91
                    print("Ladder!")
                elif (n1 == 80):
                    n1 = 99
                    print("Ladder!")
                elif (n1 == 87):
                    n1 = 36
                    print("Snake!")
                elif (n1 == 93):
                    n1 = 73
                    print("Snake!")
                elif (n1 == 95):
                    n1 = 75
                    print("Snake!")
                elif (n1 == 98):
                    n1 = 79
                    print("Snake!")
                if(n1>100):
                    print("Play another time")
                    n1=o1

                print("New Position is", n1)
                if(n1==100):
                    print("Player One Is Winner!!")
                    i=1
                    break
                o1=n1

            elif(k==2):
                k=1
                n2=r+o2
                if (n2 == 1):
                    n2 = 38
                    print("Ladder!")
                elif (n2 == 4):
                    n2 = 14
                    print("Ladder!")
                elif (n2 == 9):
                    n2 = 31
                    print("Ladder!")
                elif (n2 == 17):
                    n2 = 7
                    print("Snake!")
                elif (n2 == 21):
                    n2 = 42
                    print("Ladder!")
                elif (n2 == 28):
                    n2 = 84
                    print("Ladder!")
                elif (n2 == 51):
                    n2 = 67
                    print("Ladder!")
                elif (n2 == 54):
                    n2 = 34
                    print("Snake!")
                elif (n2 == 62):
                    n2 = 19
                    print("Snake!")
                elif (n2 == 64):
                    n2 = 60
                    print("Snake!")
                elif (n2 == 72):
                    n2 = 91
                    print("Ladder!")
                elif (n2 == 80):
                    n2 = 99
                    print("Ladder!")
                elif (n2 == 87):
                    n2 = 36
                    print("Snake!")
                elif (n2 == 93):
                    n2 = 73
                    print("Snake!")
                elif(n2 == 95):

                    n2 = 75
                    print("Snake!")
                elif (n2 == 98):
                    n2 = 79
                    print("Snake!")
                if(n2>100):
                    print("Play another time")
                    n2=o2

                print("New Position is", n2)
                if(n2==100):
                    print("Player Two Is Winner!!")
                    i=1
                    break
                o2=n2

print("Game Is Over")
