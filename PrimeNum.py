"""n = int(input())
count=0
x=0

for i in range(1,n+1):
    x+=1
if(n%i==0):
    count+=1
if(count==0):
    print("prime",x)
else:
    print("not prime",x)"""

#

n = int(input())
flag = True
x = 0
for i in range (2,int(n**0.5)+1):
    x +=1
    if(n%i==0):
        flag = False
        break
if flag == True:
    print("Prime")
else:
    print("not prime")
    
        

              
