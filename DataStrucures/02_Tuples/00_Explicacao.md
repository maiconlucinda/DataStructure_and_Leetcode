# Tuple

## O que seria uma tuple

Essencialmente uma list que eu não consigo mais alterar:

```python
myTuple = ("maicon", "lucinda", "da", "cruz", 15, 4)
```

```
índice:      0          1         2       3      4    5
        ["maicon"] ["lucinda"]  ["da"] ["cruz"] [15] [4]
```

## Como funciona

Tem ordem e tem índice igual a list, então `index`, slicing, `len` e `in` funcionam do mesmo jeito.

A diferença é que ela é **imutável**: depois de criada não existe `append`, `remove` ou trocar um valor.

E dá pra descompactar, ou seja, jogar cada posição da tuple direto em uma variável:

```python
name, sobrenome, sobrenome2, sobrenome3, dia, mes = myTuple
```
