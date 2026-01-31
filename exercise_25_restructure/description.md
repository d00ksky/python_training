
---

## 🔹 Zadanie na tę sesję (to jest „Exercise 25”)

Masz już:

* `fetch_papers(query, max_results)` ✔
* pobieranie danych ✔
* parsowanie ✔
* zapis do JSON ✔

Teraz **spinamy to w sensowne `app.py`**.

---

## 🎯 Cel

Po uruchomieniu:

```bash
python app.py transformer
```

program ma:

1. wziąć `query` z CLI
2. wywołać `fetch_papers(query)`
3. zapisać wynik do `papers.json`
4. wypisać **jedno krótkie podsumowanie**, np.:

```
Fetched 5 papers for query "transformer"
Saved to papers.json
```

I **koniec**. Żadnych dodatkowych feature’ów.

---

## 🔧 Co MA być w `app.py`

### 1️⃣ CLI (już masz, lekko)

```python
if len(sys.argv) < 2:
    print("USAGE: python app.py <query>")
    sys.exit(1)

query = sys.argv[1]
```

### 2️⃣ Wywołanie funkcji

```python
papers = fetch_papers(query)
```

### 3️⃣ Zapis do JSON

```python
data = {"papers": papers}

with open("papers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

### 4️⃣ Podsumowanie

```python
print(f'Fetched {len(papers)} papers for query "{query}"')
print("Saved to papers.json")
```

---

## ❌ Czego NIE robimy

Żeby było jasno:

* ❌ żadnych nowych funkcji
* ❌ żadnych flag
* ❌ żadnego `argparse`
* ❌ żadnego refactoru XML

To **domknięcie**, nie rozwój.

---

## ✅ Kryterium zaliczenia

Jeśli:

* program działa od CLI
* tworzy `papers.json`
* wypisuje sensowny komunikat

→ **Faza 5 jest praktycznie skończona**.

---


