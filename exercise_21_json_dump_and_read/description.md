Exercise 21 – Zapisz pobrane papery do JSON
Masz już papers jako listę słowników. Teraz:
Cel
Zapisz papers do pliku papers.json w formacie:

```
{
  "papers": [
    { "id": "...", "title": "...", "authors": ["..."] },
    ...
  ]
}
```
Wymagania

Użyj json.dump(...)

Ustaw:

indent=2
ensure_ascii=False

Po zapisie wczytaj plik z powrotem i wydrukuj:
liczbę paperów
tytuł pierwszego paperu

Zasady

Nadal standard library only
Plik zapisuj w tym samym folderze, z którego uruchamiasz skrypt
Nie kombinuj z CLI jeszcze
Minimalny hint (bo i tak dasz radę)

```
import json

data = {"papers": papers}

with open("papers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```
A potem load:

```
with open("papers.json", encoding="utf-8") as f:
    loaded = json.load(f)
```