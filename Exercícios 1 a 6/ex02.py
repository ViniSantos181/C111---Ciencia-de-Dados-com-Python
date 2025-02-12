numero = int(input("Digite um numero para ver a tabuada: "))
inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"Tabuada do {numero} de {inicio} até {fim}:")
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")