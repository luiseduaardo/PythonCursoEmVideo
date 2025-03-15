# Forma mais comum
meu_dict = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Usando a função dict()
outro_dict = dict(nome="Bob", idade=30, cidade="Rio de Janeiro")

# Criando um dicionário vazio
vazio = {}

print(meu_dict["nome"])  # Alice

print(meu_dict.get("profissao", "Não especificado"))  # Retorna "Não especificado"

meu_dict["profissao"] = "Engenheira"  # Adicionando uma nova chave
meu_dict["idade"] = 26  # Modificando um valor existente

del meu_dict["cidade"]  # Remove a chave "cidade"
profissao = meu_dict.pop("profissao")  # Remove e retorna o valor de "profissao"

# Iterando sobre as chaves
for chave in meu_dict:
    print(chave, meu_dict[chave])

# Iterando sobre os valores
for valor in meu_dict.values():
    print(valor)

# Iterando sobre os pares chave-valor
for chave, valor in meu_dict.items():
    print(f"{chave}: {valor}")

print(meu_dict.keys())    # dict_keys(['nome', 'idade'])
print(meu_dict.values())  # dict_values(['Alice', 26])
print(meu_dict.items())   # dict_items([('nome', 'Alice'), ('idade', 26)])
