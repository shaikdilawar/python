dic  = {1:'Car',2:'Apple',3:6,4:8.9}
print(dic)

dic = {'Car':['Wagnor','Benz',457949],'marks':(89,75,76),3:5}
print(dic)

dic = {'Car':{'Wagnor','Benz',457949},
       'marks':{89,75,76}}
print(dic)

d={}
d[1] = 'Audii'
print(d)
d[2] = 'Java'
print(d)
d[1] = 'Python'
print(d)

#converting
di = [(1,'a'),(2,'b'),(3,'c')]
print(di)
di = dict(di)
print(di)

#indirect way of creating dictionary
#method 1
keys = [1,2,3,4]
values = ['a','b','c','d']
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)
#method 2
n= int(input())
l = []
for i in range(n):
    k = int(input())
    v = input()
    l.append((k,v))
print(l)
d = dict(l)
print(d)
