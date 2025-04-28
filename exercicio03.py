nomes=["João","Carlos","Ana","Maria","Pitomba"]

pesquisa=input("Digite um nome: ")
for x in range(len(nomes)):
    if pesquisa== nomes[x]:
        print(f"Achei o misera {nomes[x]} na posição {x}")