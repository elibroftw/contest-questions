lines = int(input())
list=[]
wait=[0]
out=[]
put=[]
for i in range(0,lines):
    way=1
    time=0
    activity=input()
    if (activity[0:1]== 'R' and out.count(activity[2:])==0):
        out.append(activity[2:])
        put.append(0)
    if activity[0:1]=='W': way=int(activity[2:])-1
    wait.append(way)
    list.append(activity)
    if activity[0:1]=='S':
        for x in range(list.index('R '+activity[2:])+1,list.index(activity)+1):
            time=time+wait[x]
        out.sort()
        y=put.pop(out.index(activity[2:]))
        put.insert(out.index(activity[2:]),y+time)
        list.insert(list.index('R '+ activity[2:]),'W')
        list.remove('R '+ activity[2:])
        list.remove(activity)
        list.append('W')
for x in list:
    if x[:1]=='R':
        if out.count(x[2:])>0:
            put.pop(out.index(x[2:]))
            out.remove(x[2:])
        out.append(x[2:])
        out.sort()
        put.insert(out.index(x[2:]),'-1')
for i in range(0,len(out)):
    print(out[i],put[i])
