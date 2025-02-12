nome_completo = input("Digite seu nome completo: ")

print("Nome em maiusculas:", nome_completo.upper())
print("Nome em minusculas:", nome_completo.lower())
print("Numero de letras no nome:", len(nome_completo.replace(" ", "")))

partes_nome = nome_completo.split()
if len(partes_nome) > 1:
    partes_nome[-1] = "do Inatel"
    novo_nome = " ".join(partes_nome)
else:
    novo_nome = nome_completo + " do Inatel"

print("Nome modificado:", novo_nome)