palavra = input("Digite uma palavra: ")

vogais = 0
tem_a = False

for letra in palavra:
    print(letra.upper())
    if letra.lower() in "aeiou":
        vogais += 1
    if letra.lower() == "a":
        tem_a = True

print(f"Quantidade de vogais: {vogais}")
print(f"A letra 'A' está presente: {'Sim' if tem_a else 'Não'}")
