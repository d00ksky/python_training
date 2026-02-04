Wiem. I masz rację **odczuciowo**. Te zadania się dłużą.
Ale **obiektywnie** jesteś **jedno ćwiczenie** od projektu. To nie jest pocieszanie, to stan faktyczny.

Powód, dla którego to męczy:

* zadania są **proste**
* a proste rzeczy są **mentalnie irytujące**, gdy już widzisz projekt w głowie
* mózg krzyczy: „po co ja to jeszcze robię, przecież umiem”

I właśnie dlatego większość ludzi:

* przeskakuje ten moment
* wchodzi w projekt
* potem tonie w chaosie

Ty akurat robisz to **jak inżynier**, nie jak entuzjasta z YouTube’a.

---

## Dobra, skracamy dystans

### To jest **OSTATNIE** ćwiczenie przed projektem

Po nim **oficjalnie** mówię: *start arXiv app*.

---

## Final Calibration Exercise

Masz **dwie funkcje**, które już umiesz pisać:

```python
fetch_papers(query) -> list[dict]
normalize_titles(titles) -> list[str]
```

### Zadanie

Napisz funkcję:

```python
def get_normalized_titles(query: str) -> list[str]:
```

Która:

1. pobiera papers przez `fetch_papers`
2. wyciąga z nich **same tytuły**
3. normalizuje je przez `normalize_titles`
4. zwraca listę stringów

### Zasady

* żadnych globali
* żadnych printów
* zero logiki „w locie”
* tylko **składanie funkcji**

Schemat:

```text
query
  ↓
fetch_papers
  ↓
lista dictów
  ↓
lista tytułów
  ↓
normalize_titles
  ↓
wynik
```

---

To ćwiczenie:

* NIE uczy nowej składni
* sprawdza tylko jedno: **czy potrafisz myśleć pipeline’em**

Zrób to spokojnie.
Wklej **tylko funkcję**.

Jak to przejdzie:

> **zamykamy trening i zaczynamy projekt**

Serio. Bez kolejnych „jeszcze jednego zadania”.
