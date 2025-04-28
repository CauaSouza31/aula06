a=['']*5
m=['']*5
x=0

for i in range(len(a)):
    a[1]=int(input("digite um numero: "))

x=int(input("Digite o multiplicador: "))
for y in range(len(m)):
    m[y]=x*a[y]
print(a)
print(x)
print(m)