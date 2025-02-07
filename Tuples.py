#tuples are immutable
t = ()
print(t)

t = (4,2,8,6,1)
print(sorted(t))
print(t)

print(dir(t))

#input
t = tuple(map(int,input().split()))
print(t)

#slice [start:end:step]
l = [1,2,3,4,5,6,7,8,9,10]
print(l[2:10])
print(l[2:10:2])
#if step is -ve it will print reverse 
print(l[::-1])
print(l[2:8:-1])
print(l[8:2:-1])
print(l[5:1:-3])
#python supports -ve indexing as well

