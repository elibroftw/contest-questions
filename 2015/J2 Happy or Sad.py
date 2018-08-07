msg=input()
y=3
happy=0
sad=0
for i in range(0,len(msg)):
               if msg[i:y]==':-)': happy=happy+1
               if msg[i:y]==':-(': sad=sad+1
               y=y+1
if happy>sad: print('happy')
if sad>happy: print('sad')
if sad==0 and happy==0: print('none')
elif sad==happy: print('unsure')
