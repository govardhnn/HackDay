lf=list()
li=['a','g',1,2,7,8]
def grab():
    for i in range(len(li)):
        if type(li[i])==int:
            lf.append(li[i])
grab()
print(lf)