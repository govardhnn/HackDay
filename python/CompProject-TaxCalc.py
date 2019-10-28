txlst="""1.Income Tax
2.Sales Tax
3.Property Tax
4.Road Tax
5.Luxury Tax
6.Custom Duty
7.Excise Duty
8.Corporation Tax"""

def intro():
    taxid=input("Enter your tax id:")
    print(txlst)
    srn=input("Enter the serial no of the tax to be paid, separated by a comma : ")
    ser=srn.split(",")
    return(ser)

def income():
    inc=input("Enter your income")
    try:
        if(inc in range(100000)):
            tax=inc*0.1
#     except:
#         print("incorrect")
        
def sales():
    print("eg")
def prop():
    print("eg")
    

ldic={"1":income,"2":sales,"3":prop}
def evaluate(n):
    ldic[n]()
l=intro()
length=len(l)
for i in l:
    evaluate(i)



