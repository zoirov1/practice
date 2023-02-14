
a = list(map(int,input('>> ').split()))
ls = []
mx_sub=0
for i in range(1,len(a)):
    lc_sub=abs(a[i]-a[i-1])
    if lc_sub>=mx_sub:
        x=a[i-1]
        y=a[i]
        mx_sub=lc_sub
        ls.append([mx_sub,f"{mx_sub}({x} va {y})"])
ls2 = []

mx=ls[0][0]
for j in ls:
    if j[0]>mx:
        mx=j[0]

for k in ls:
    if k[0]==mx:
        ls2.append(k[1])

print(ls2)




