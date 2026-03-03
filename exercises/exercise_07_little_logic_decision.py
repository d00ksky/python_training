#_________________________________________________________________________
# ## Phase 2 – Exercise 7: Mała decyzja logiczna

# Ostatnie ćwiczenie na dziś. Krótkie, ale ważne.

# ### Zadanie

# Napisz funkcję:

# ```python
# def has_any_long_papers(papers):
#     ...
# ```

# która:

# * przyjmuje listę tytułów
# * zwraca `True`, jeśli **chociaż jeden** tytuł ma długość >= 20
# * w przeciwnym razie zwraca `False`

# ### Zasady

# * Jedna pętla
# * **Nie** twórz dodatkowych list ani słowników
# * Zwróć wynik **jak najszybciej**, gdy to możliwe
# * Funkcja **zwraca bool**, nie drukuje

# To ćwiczenie uczy **kontroli przepływu**, nie struktury danych.

# Pisz kod.
#_________________________________________________________________________

papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]

def has_any_long_papers(papers):
    for title in papers:
        if len(title) >= 20:
            return True
    return False

print(has_any_long_papers(papers))