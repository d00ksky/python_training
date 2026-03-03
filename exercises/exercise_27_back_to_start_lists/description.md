
## Exercise 2 (wracamy do tego, co przerwaliśmy)

Napisz funkcję:

```python
def normalize_titles(titles: list[str]) -> list[str]:
```

Wymagania:

* usuwa puste stringi (po stripowaniu)
* usuwa spacje z początku i końca
* zamienia wielokrotne spacje wewnątrz na jedną
  (bez regexów, bez bibliotek)
* kapitalizuje tylko pierwszą literę całego tytułu
  (`"deep learning"` → `"Deep learning"`)

Przykład:

Wejście:

```python
[
    "  deep   learning  ",
    "",
    "quantum    computing",
    " ai ",
    "   "
]
```

Wyjście:

```python
[
    "Deep learning",
    "Quantum computing",
    "Ai"
]
```

Zasady:

* bez `print`
* bez globali
* tylko funkcja

Wklej **tylko kod funkcji**.
