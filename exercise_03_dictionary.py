#__________________________________________________________________________________________________
# ## Exercise 3: Słowniki (dict), bez udawania mądrości

# Teraz dokładamy **strukturę**, bo bez tego żadnego arXiva nie zrobisz.

# ### Zadanie

# Masz listę tytułów `papers`.

# 1. Utwórz słownik `paper_lengths`, gdzie:

#    * klucz → tytuł
#    * wartość → długość tytułu (liczba znaków)

# 2. Utwórz listę `long_papers`, która zawiera **tylko tytuły**, których długość:

#    * jest **większa lub równa 20**

# 3. Wydrukuj:

# ```text
# Paper lengths: { ... }
# Long papers: [...]
# ```

# ### Zasady

# * Jedna pętla `for`.
# * Zero ręcznych liczników.
# * Zero list comprehensions.
# * Czytelne nazwy.

# Pisz kod.
#__________________________________________________________________________________________________

papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]
paper_lengths = {}
long_papers = []

for title in papers:
    length = len(title)
    paper_lengths[title] = length
    if length >= 20:
        long_papers.append(title)
    
print(f"Paper lengths: {paper_lengths}")
print(f"Long papers: {long_papers}")