while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo == "M":
        print("Sexo masculino registrado.")
        break
    elif sexo == "F":
        print("Sexo feminino registrado.")
        break
    else:
        print("Entrada invalida! Tente novamente.")