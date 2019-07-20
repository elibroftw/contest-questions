mins=int(input()) #
hours,time,out=0,0,0
if mins>=60: hours,mins=(mins//60),mins-(mins//60)*60
  
if hours>=12: out,hours=(hours//12)*31,hours-(hours//12)*12

if hours>0: hours,mins=0,hours*60+mins

for i in range(0,mins):
    time=time+1
    if time==60: hours,time=hours+1,0
    hourmins=str(hours)+str(time)
    if (hourmins=='034' or hourmins=='111' or hourmins=='123' or hourmins=='135' or
        hourmins=='147' or hourmins=='159' or hourmins=='210' or hourmins=='222' or
        hourmins=='234' or hourmins=='246' or hourmins=='258' or hourmins=='321' or
        hourmins=='345' or hourmins=='333' or hourmins=='357' or hourmins=='444' or
        hourmins=='456' or hourmins=='432' or hourmins=='420' or hourmins=='555' or
        hourmins=='543' or hourmins=='531' or hourmins=='654' or hourmins=='642' or
        hourmins=='630' or hourmins=='753' or hourmins=='741' or hourmins=='852' or
        hourmins=='840' or hourmins=='951' or hourmins=='1111'):out=out+1
#print(mins)
print(out)
