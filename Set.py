"""set is mutable
doesnot contain duplicates and unindexed and unordered"""

s = set()
print(s,type(s))

s = {1,2,3,4,5}
s = {1,2,3,44,5}
print(s)

s = {4,'c',"Sri indu",8.9,2,4}
print(s)

#input
s = set(map(int,input().split()))
print(s)

#frozenset-immutable
s = frozenset([3,'pyhton',5.7])
print(s)
