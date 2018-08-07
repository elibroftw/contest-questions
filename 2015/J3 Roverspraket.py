origin=input()
x=0
y=1
for i in range(0,len(origin)):
               if (origin[x:y]== 'a' or origin[x:y]== 'e' or origin[x:y]== 'i'
                   or origin[x:y]== 'o' or  origin[x:y]== 'u'):
                   x=x+1
                   y=y+1
                   continue
               r=1
               while True:
                       temp=ord(origin[x:y])
                       if (temp-r==97 or temp-r==101 or temp-r== 105 or
                           temp-r==111 or temp-r==117):
                               temp=chr(temp-r)
                               break
                       if (temp+r==97 or temp+r==101 or temp+r== 105 or
                           temp+r==111 or temp+r==117):
                               temp=chr(temp+r)
                               break
                       r=r+1
               while True:
                       tempf=ord(origin[x:y])
                       if chr(tempf) =='z':
                           tempf='z'
                           break
                       if (tempf+1==97 or tempf+1==101 or tempf+1==105 or
                           tempf+1==111 or tempf+1==117):
                            tempf=chr(tempf+2)
                            break
                       else:
                           tempf=chr(tempf+1)
                           break
               origin=origin[:y]+temp+tempf+origin[y:]
               y=y+3
               x=x+3
print(origin)
