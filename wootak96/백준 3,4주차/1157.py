list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
d=input()
a=d.upper()
length=len(a)

for i in range(length):
    for k in range(len(list)):
        if a[i]==chr(65+k):
           list[k]=list[k]+1
            

maxnum=max(list)

maxcount=list.count(maxnum)

if maxcount>1:
    print('?')
else :
    x=list.index(maxnum)
    print(chr(65+x))
