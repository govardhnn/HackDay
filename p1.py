'''n=int(input("Enter a number"))
s=0
p=1
while(n>0):
    s=s+n
    p=p*n
    n=n-1
#for i in range(n):
 #   s+=i+1
  #  p=p*(i+1)
print(s,p,sep=" ")    
'''
'''
l="STRING"
ln=len(l)
for i in range(ln):
    print (i,l[i])
    '''
'''print(type(True))
print(0B1101)'''
#why did you comment the above
i=(1,10,True)
for l in i:
    while(True):
        if(type(i)==int):
            print(i)
            continue
        elif(type(i)==bool):
            print(i)
            exit
