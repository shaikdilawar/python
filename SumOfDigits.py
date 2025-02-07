n = int(input())
sume=0
rem=0
while(n>0):
    rem=n%10
    sume+=rem
    n=n//10
print(sume)
