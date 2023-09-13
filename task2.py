import random
import time

print("Park RunTimer")
print("-------------\n")
print("lets Go\n")
time=[100,200,300,400,500,600,700,800]
runner={101:200,102:300,103:30,104:700,105:450,106:900,106:208,107:750}
l1=[]
l2=[]
t=random.choice(time)
for i,j in runner.items():
  
    if j in range(0,t):
        print(">"+str(i)+"::"+str(j))
        l1.append(j)
        l2.append(i)

print(">End\n")
l=len(l1)
print("total Number of Runner:"+str(l))
avg=sum(l1)/len(l1)
#print("average time:"+str(avg))
m,s=divmod(int(avg),60)
print("average time: "+ str(m)+" minutes "+str(s)+" seconds ")
fast=max(l1)
#print(fast)
fast_m,fast_s=divmod(fast,60)
print("fastest time: "+ str(fast_m)+" minutes "+str(fast_s)+" seconds ")
slow=min(l1)
slow_m,slow_s=divmod(slow,60)
print("slowest time: "+ str(slow_m)+" minutes "+str(slow_s)+" seconds ")
idx=l1.index(slow)
print("Best time runner is #"+str(l2[idx]))