l=i=j=psum=0
ch=int(input("Enter the choice for nth number in series"))

for i in range(100):
    string=str(i)
    psum=0
    for j in string:
        psum+=int(j)
        if(psum==10):
            print(string)
            list1[j]=int(j)
            
            
            
    