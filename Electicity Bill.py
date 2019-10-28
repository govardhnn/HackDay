#Electricity Bill
'''
base value-70
1-100;2.2
(220)
100-200;3.1
(530)
200-300;4.4
(970)
>300;5.5
tax is 8% on final value
'''
base=70
un=int(input('Enter the "Total Units" Consumed  '))

if(un<=100):
    unprice=(un*2.2)
    
elif(un>100 and un<=200):
    run=un-100
    unprice=(run*3.1)+220
    
elif(un>200 and un<=300):
    run=un-200
    unprice=(run*4.4)+530
    
elif(un>300):
    run=un-300
    unprice=(run*5.5)+970
    
tax=unprice*8/100
tot=tax+unprice
print("The total Electricity Bill is: {} rupees inclusive of tax: {} rupees".format(int(tot),int(tax)))


    