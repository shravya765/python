x = [ 1 , 2 , 4, 5]
for i in x:
    print(i)
print(list(x))
x.insert(2,22)
print(x)
x.append(50)
print(x)
print(x.index(2))
y = x.copy()
print(y)
x.remove(1)
print(x)
x.pop(4)
print(x)
z = [ 7 , 8, 9]
x.extend(z)
print(x)
x.sort(reverse= True)
print(x)
x.sort(reverse= False)
print(x)
for p in x:
    print(p ** p)
x.reverse()
print(x)
x.clear()
print(x)