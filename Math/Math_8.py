x = input()

a = str((int(x) % 10))
b = str((int(x) % 100) // 10)
c = str(int(x) // 100)

n = c + a + b 
s = b + c + a
w = b + a + c
z = a + c + b 
v = a + b + c

print(x)
print(n)
print(s)
print(w)
print(z)
print(v)