# IMUTÁVEL - Depois de criado, nao consigo mais alterar

myTuple = ("maicon", "lucinda", "da", "cruz", 15, 4)

# Conta quantas vezes o valor que passei aparece na tuple.
print(myTuple.count("da"))

# Busco por um valor e recebo um indice.
print(myTuple.index(15))


# Posso fazer slicing tambem
print(myTuple[0:4])

# Posso chamar o len()
print(len(myTuple))

# Posso testar se algo existe na tuple
print(15 in myTuple)

# Posso descompactar 
name, sobrenome, sobrenome2, sobrenome3, dia, mes = myTuple


