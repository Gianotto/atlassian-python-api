import random

# criar uma lista de produtos e preços
produtos = ["camiseta", "calça", "tênis", "meia", "shorts"]
precos = [20.00, 50.00, 100.00, 10.00, 30.00]

# combinar os produtos e preços em uma lista de tuplas
lista_produtos_precos = list(zip(produtos, precos))

# randomizar a lista de produtos e preços
random.shuffle(lista_produtos_precos)

# imprimir a lista randomizada
print("Lista de produtos e preços randomizados:")
for produto, preco in lista_produtos_precos:
    print(f"{produto}: R${preco:.2f}")
