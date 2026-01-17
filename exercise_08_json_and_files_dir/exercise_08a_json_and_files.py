#____________________________________________________________________________________________________

# ## Phase 3 – Exercise 8: JSON + pliki (bez czarów)

# To jest **pierwsze zadanie**, które symuluje prawdziwą pracę. Nadal proste, ale już użyteczne.

# ### Zadanie

# 1. Masz listę tytułów `papers` (jak zawsze).
# 2. Napisz funkcję:

# ```python
# def save_papers_to_json(papers, filepath):
#     ...
# ```

# która:

# * zapisuje dane do pliku JSON pod `filepath`
# * format danych w pliku ma być dokładnie taki:

# ```json
# {
#   "papers": [
#     "Attention Is All You Need",
#     "GANs in Action",
#     "A Survey on Transformers"
#   ]
# }
# ```

# 3. Napisz drugą funkcję:

# ```python
# def load_papers_from_json(filepath):
#     ...
# ```

# która:

# * wczytuje plik JSON
# * **zwraca listę tytułów** (czyli wartość spod klucza `"papers"`)

# 4. Na końcu:

# * zapisz plik
# * wczytaj go z powrotem
# * `print()` wczytaną listę, żeby potwierdzić, że działa

# ---

# ### Zasady (ważne, czytaj)

# * Użyj modułu `json` z biblioteki standardowej
# * Funkcje **nie drukują**, tylko robią swoją robotę
# * `print()` tylko w części testowej
# * Zero globalnych zmiennych w funkcjach
# * Kod ma działać po odpaleniu pliku `.py`

# ---

# ### Hint (tylko jeden, bo nie jesteśmy w przedszkolu)

# * `json.dump(...)` zapisuje do pliku
# * `json.load(...)` czyta z pliku
# * pliki otwieramy przez `with open(...) as f:`

# ---

# To zadanie:

# * uczy pracy z IO
# * przygotowuje grunt pod CLI
# * jest 1:1 tym, co będziesz robił z danymi z arXiva

# Pisz kod.
# Jak to przejdzie czysto, w następnym kroku zrobimy **mini-narzędzie z argumentami z terminala**.
#____________________________________________________________________________________________________

import json

papers = [
    "Attention Is All You Need",
    "GANs in Action",
    "A Survey on Transformers"
]

data = {
    "papers": papers
}

with open("papers.json", "w") as f:
    json.dump(data, f)

with open('papers.json') as f:
    data = json.load(f)
    
print(data)
print(data["papers"])

    


    

