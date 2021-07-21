# Expressões Regulares com Python

## Metacaracteres

`. ^ $  [ ]  \  |  -`

- `|` → ou
- `.` → qualquer caractere (com exceção da quebra de linha)
- `[]` → conjunto de caracteres
- `-` → qualquer entre (a-z)

## Quantificadores

`* + ?  { } ( )`

- `*` → 0 ou n  caracteres
- `+` → 1 ou n caracteres (caractere a esquerda)
- `?` → 0 ou 1 caractere
- `{ }` → {n} caracteres ou {min, max} caracteres

### Grerdy Non-Greedy (Lazy)

Por padrão o regex se comportará de forma gulosa, ou seja, analisará a string toda para achas as expressões regulares. com o auxilio do quantificador `?` é possível mudar esse comportamento.


## Como utilizar no Python

```python
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re

re.search(regex, text)     # acha a primeira ocorrencia do regex
re.findall(regex, text)    # acha todas as ocorrencias do regex
re.sub(regex, sub, text)   # substitui o regex pelo sub
re.compile(regex)          # compila o regex (util quando se vai usar em mais de uma parte do codigo

# Flags
re.IGNORECASE              # ignora se o(s) são maiusculos ou minusculos
```
