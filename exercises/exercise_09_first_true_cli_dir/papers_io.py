#_______________________________________________________________________________________
# ## **Exercise 9: Pierwsze prawdziwe CLI**

# ### Cel

# Chcę, żebyś mógł uruchomić program tak:

# ```bash
# python app.py save papers.json
# python app.py load papers.json
# ```

# I żeby on **robił sensowne rzeczy**.

# ---

# ### Założenia

# Masz już (albo masz napisać jeszcze raz, spokojnie):

# * `save_papers_to_json(papers, filepath)`
# * `load_papers_from_json(filepath)`

# Teraz zrobimy **warstwę sterującą**.

# ---

# ## Zadanie

# Napisz plik `app.py`, który:

# 1. Czyta argumenty z linii poleceń (`sys.argv`)
# 2. Obsługuje **dwie komendy**:

#    * `save`
#    * `load`

# ### Zachowanie programu

# #### Jeśli użytkownik wpisze:

# ```bash
# python app.py save papers.json
# ```

# Program:

# * zapisuje **hardcoded** listę `papers` do pliku `papers.json`
# * drukuje:

# ```text
# Saved papers to papers.json
# ```

# #### Jeśli użytkownik wpisze:

# ```bash
# python app.py load papers.json
# ```

# Program:

# * wczytuje plik
# * drukuje listę papers (normalny `print`)

# ---

# ## Zasady (czytaj, bo tu ludzie robią chaos)

# * Użyj `import sys`
# * Nie używaj żadnych zewnętrznych bibliotek
# * Nie obsługuj jeszcze błędów
# * Jeśli argumentów jest za mało → program może się wysypać, **to jest OK**
# * Logika CLI **nie siedzi w funkcjach zapisu/odczytu**

# ---

# ## Hint (jeden, koniec)

# ```python
# sys.argv[0]  # nazwa pliku
# sys.argv[1]  # komenda
# sys.argv[2]  # filepath
# ```

# ---

# To ćwiczenie:

# * łączy wszystko, co już zrobiłeś
# * pokazuje sens jawnych kontraktów
# * jest fundamentem pod arXiv CLI

# Pisz kod.
# Jak to przejdzie, zaczniemy go **czyścić i utwardzać** jak normalne narzędzie.
#_______________________________________________________________________________________

import json


def save_papers_to_json(papers, filepath):
    data = {'papers': papers}
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
        
def load_papers_from_json(filepath):
    with open(filepath) as f:
        read_data = json.load(f)
    return read_data["papers"]
    

