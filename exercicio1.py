nome_completo = input("Digite seu nome completo: ")

maiusculas = nome_completo.upper()
minusculas = nome_completo.lower()
total_letras = sum(1 for c in nome_completo if c.isalpha())

partes_nome = nome_completo.split()
partes_nome[-1] = "do Inatel"
nome_com_inatel = " ".join(partes_nome)

print(f"Nome em maiúsculas: {maiusculas}")
print(f"Nome em minúsculas: {minusculas}")
print(f"Total de letras: {total_letras}")
print(f"Nome com 'do Inatel': {nome_com_inatel}")
