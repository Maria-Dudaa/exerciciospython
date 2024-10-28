def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    resultado = fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}.")
