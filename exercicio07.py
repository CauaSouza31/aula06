nome=[""]*5
senha=[""]*5

for x in range(len(nome)):
    nome=input("Digite seu nome: ")
    print(nome)
print(f"-------------------------------------------------")
for y in range(len(senha)):
   senha=int(input("Digite sua senha:"))
   print(senha)
print(f"-------------------------------------------------")
print(f"Nome:{nome} Senha:{senha}")
