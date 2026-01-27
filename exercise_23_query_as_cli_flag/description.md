

---

## Następny krok: Exercise 23 — `query` z CLI

### Cel

Zamiast:

```python
query = "transformer"
```

chcemy:

```bash
python app.py transformer
```

I żeby:

* `transformer` trafiło do zapytania arXiv
* reszta pipeline’u została **nietknięta**

---

## Minimalny zakres (ważne)

Na tym etapie:

* ❌ żadnych flag typu `--query`
* ❌ żadnych parserów (`argparse`)
* ❌ żadnych subkomend

Tylko:

```python
import sys
query = sys.argv[1]
```

Jeśli argumentu brak:

* wypisujesz krótkie usage
* `sys.exit(1)`

To wszystko.

---

## Dlaczego NIE robimy flag jeszcze

Bo flagi:

* są tylko interfejsem
* nie zmieniają architektury
* łatwo je dodać później

Teraz interesuje nas **przepływ danych**:
CLI → query → URL → HTTP → XML → JSON

Jak to będzie stabilne, wtedy:

* rozbijemy na funkcje
* dodamy `argparse`
* dołożymy opcje typu `--max-results`

---

## Mała uwaga, bo zaraz na to wpadniesz

Tak, docelowo to będzie wyglądać jak:

```bash
python app.py fetch transformer --limit 10
```

Ale **nie teraz**.
Teraz robimy wersję „kamienną”, która działa i jest zrozumiała.

---

## Podsumowanie w jednym zdaniu

Tak — **CLI jako źródło `query` to dokładnie następny krok**,
a to, że to przewidziałeś, oznacza, że **zaczynasz myśleć jak autor programu, nie jak wykonawca ćwiczeń**.

Rób Exercise 23 spokojnie. Jak skończysz, nie wklej całego pliku — tylko fragment z `sys.argv` i budowaniem URL.
