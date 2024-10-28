def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

entrada = input("Digite uma palavra: ")

if palindromo(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')
