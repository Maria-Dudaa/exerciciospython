# 1. Criando o dicionário vazio
pessoas = {}

# 2. Adicionando pessoas com nome e idade
pessoas["Alice"] = 30
pessoas["Bob"] = 25
pessoas["Charlie"] = 35

# 3. Exibindo as informações de todas as pessoas
for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")
