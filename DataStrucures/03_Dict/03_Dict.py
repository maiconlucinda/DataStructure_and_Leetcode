
myDict = {"name": "Maicon", "idade": 26, "Cor": "preta"}

# ACCESS
print(myDict["name"]) # Gives an erros if the key does not exist
print(myDict.get("name"))
print(myDict.get("x", 0)) # Retorna 0 caso a chafe x nao existir

# Retorna lista com todas as keys
print(myDict.keys())

# Retorna lista com todos os valores
print(type(myDict.values()))


# REMOVER
# Remove a chave/valor que foi passado
print(myDict.pop("Cor")) # Retorna o valor. Erro se nao existir

myDict.pop("Cor", None) # Nao gera erro se nao existir


print(myDict)