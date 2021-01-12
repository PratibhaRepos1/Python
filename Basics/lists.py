# Comprehenssive

l = []
for x in range(0,10):
    l.append(x)

#print(l)

#another way
l = [x for x in range(0,15)]
t = tuple(x for x in range(0,15))
s={x for x in range(0,15)}
d = {x: x*x for x in range(0,15)}

print(l)
print(t)
print(s)
print(d)