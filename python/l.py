i=0
'''l=int(input("Enter the length of the list"))
for i in range(l):
    list1[i]=int(input("Enter the number"))'''

tsum=osum=esum=0
list1=[5,-1,7,9,6,-8,-9]
l=len(list1)
print("The list is",list1)
while l>0:
    tsum=tsum+list1[l-1]
    if list1[l-1]%2==0:
        esum=esum+1
    else:
        osum=osum+1
    l=l-1
    
print(esum,osum,tsum)