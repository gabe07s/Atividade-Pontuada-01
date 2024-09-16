import os
os.system('clear || cls')

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
notageral = 0
media_pares = 0
media_impares = 0
media_geral = 0
lista = []

# Solicitar e informar o que os números representam
for i in range(5):
    notageral = int(input(f"Digite o {i+1}º número: "))
   # Processando cada número
    if notageral % 2 == 0:
        quantidade_pares += 1
        soma_pares += notageral
        media_pares = soma_pares / quantidade_pares 
    else:
        quantidade_impares += 1
        soma_impares += notageral
        media_impares = soma_impares / quantidade_impares

    if notageral < 0:
        quantidade_negativos += 1
    else:
        quantidade_positivos += 1
    soma_geral += notageral
    lista.append(notageral)

maior_numero = max(lista)
menor_numero = min(lista)

# Calculando as médias
media_geral = soma_geral / 5

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}\n")
for i, numero in enumerate(reversed(lista)):
    print(f"{len(lista)-i}º - {numero}")