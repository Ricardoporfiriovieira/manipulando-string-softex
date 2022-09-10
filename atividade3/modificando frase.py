frase = input("Digite uma frase: ")

minusculo = frase.lower()

mudar = input("Digite a palavra que você deseja modificar: ")
novapalavra = input("Digite a nova plavra para substituir a antiga: ")

novafrase = minusculo.replace(mudar, novapalavra)

print(f"Resultado após modificação: {novafrase}")