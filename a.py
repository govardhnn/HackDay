# cook your dish here
from collections import defaultdict
for z in range(int(input())):
    d=defaultdict(list)
    for y in range(12):
        h,gh,v,ga,a=input().split()
        gh=int(gh)
        ga=int(ga)
        if d[h]:d[h][1]+=gh-ga
        else:
            d[h].append(0)
            d[h].append(gh-ga)
        if d[a]:d[a][1]+=ga-gh
        else:
            d[a].append(0)
            d[a].append(ga-gh)
        if gh>ga:d[h][0]+=3
        elif gh<ga:d[a][0]+=3
        else:
            d[h][0]+=1
            d[a][0]+=1
    sd=sorted(d.items(),key=lambda e:(-e[1][0],-e[1][1]))
    print(sd[0][0],sd[1][0])