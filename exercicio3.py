sexo = input("Digite o sexo (M/F): ").strip().upper()

while sexo != "M" and sexo != "F":
    sexo = input("Sexo inválido. Digite novamente (M/F): ").strip().upper()

if sexo == "M":
    print("A pessoa é homem.")
else:
    print("A pessoa é mulher.")
