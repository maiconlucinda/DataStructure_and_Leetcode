# Dict

## O que seria um dict

Uma estrutura de pares, onde cada chave aponta para um valor:

```python
myDict = {"name": "Maicon", "idade": 26, "Cor": "preta"}
```

```
chave       valor
"name"   →  "Maicon"
"idade"  →  26
"Cor"    →  "preta"
```

## Como funciona

Aqui eu não chego no valor pelo índice, eu chego pela **chave**.

São duas formas de acessar, e elas se comportam diferente quando a chave não existe:

```python
myDict["x"]        # erro
myDict.get("x")    # None
myDict.get("x", 0) # 0 (valor padrão que eu escolhi)
```

O mesmo vale para remover: `pop("Cor")` dá erro se não existir, `pop("Cor", None)` não.
