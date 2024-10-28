def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite o número que deseja saber se é primo: "))

if primo(numero):
    print("O número informado é primo.")
else:
    print("O número informado não é primo.")
