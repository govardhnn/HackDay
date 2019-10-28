'''def funct(t,u):
    t=int(t)
    u=int(u)
    s=t+u
    p=t*u
    pw=t**u
    return(print(s,p,pw,sep=" "))
(t,u)=tuple(input("Enter the two numbers"))
funct(t,u)'''
def pattern(s,t):
    while(s.isalpha()):
        print(s*t)
        exit()
    
l=tuple(input("Enter the two keys"))
s=l[0]
t=int(l[1])
pattern(s,t)