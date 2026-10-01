# Set

## O que seria um set

Um conjunto de valores únicos, sem ordem:

```python
mySet = {1, 2, 3}
```

```
{ 1 , 2 , 3 }
  ↑
  sem índice, sem posição fixa
```

## Como funciona

É **mutável**, então eu consigo adicionar e remover.

Mas não tem ordem, ou seja, não existe índice nem slicing, e o `pop()` remove um item qualquer.

E não aceita **duplicatas**: se eu adicionar um valor que já está lá, nada acontece.

```python
mySet = {1, 2, 3}
mySet.add(3)   # continua {1, 2, 3}
```

Assim como no dict, remover tem as duas versões: `discard` não dá erro se não existir, `remove` dá.
