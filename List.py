"""represented in []
contains heterogeneous mixture of values
is mutable
is orderedd contains duplicates"""


l = []
print(l)

l = [1,2,3,3,4]
print(l)

l = [1.1,4.5,2.3,5.5]
print(l)

l = [1.5,6,'sri indu','d']
print(l)

#input 
l = list(map(int,input().split()))
print(l)

l=[1,3,5,7,9]
#using index
for i in range(len(l)):
    print(l[i],end=" ")

print()
#without index
for i in l:
    print(i,end=" ")
