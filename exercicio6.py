nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))

soma = nota1 + nota2 + nota3 
media = soma / 3

if media < 7:
    print("Seu aluno foi reprovado.")
else:
    print("Seu aluno foi aprovado!")