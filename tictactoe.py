

winner=False

def display():
    global listf
    print(listf[0])
    print(listf[1])
    print(listf[2])
    return()
    
def p1():
    global listf
    posr=int(input("Enter the row"))
    posc=int(input("Enter the column"))
    r=posr
    c=posc
    listf[r][c]="0"

    

def p2():
    global listf
    posr=int(input("Enter the row"))
    posc=int(input("Enter the column"))
    r=posr
    c=posc
    listf[r][c]="X"
    
def check():
    for x in range(0,3):
        if (listf[x][0] == listf[x][1] and listf[x][0] == listf[x][2] ):
            winner = True
        elif (listf[0][x] == listf[1][x] and listf[0][x] == listf[2][x] ):
            winner = True
    
    return()
k=0
while(k==0):
       
    p1()
    display()   
    check()    
    if(winner==True):
        print("player 1 wins")
        k=1    
    p2()
    display()
    check()
    if(winner==True):
        print("player 2 wins")
        k=1

    



        
        