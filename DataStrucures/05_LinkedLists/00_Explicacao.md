# Linked List

## O que seria um node

Essencialmente um dicionário:

```python
head = {
    "value": 4,
    "next": {
        "value": 7,
        "next": {
            "value": 4,
            "next": None   # tail
        }
    }
}
```

## Como funciona

O `next` sempre aponta diretamente para o outro "dicionário", ou seja, o valor do próximo node.

E temos também um `head`, que seria o primeiro node, e o `tail`, que seria o último node.

```
head        tail
 ↓           ↓
[4] → [7] → [4] → None
```
