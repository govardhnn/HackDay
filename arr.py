import random
def tr():
    sum=0
    for i in range(5):
        a=random.randint(0,1)
        sum+=a
    return(sum)
for i in range(5):
    sum=tr()
    if(sum==2 or sum==3):
        print("I knew it")
    else:
        print("oho")
