#_____________________________________________________________________________________________
# ## Exercise 4: Funkcje. W końcu.

# Teraz przestajemy pisać kod „od góry do dołu jak notatnik”.

# ### Zadanie

# Napisz **funkcję**:

# ```python
# def analyze_papers(papers):
#     ...
# ```

# która:

# 1. Przyjmuje listę tytułów
# 2. Zwraca **krotkę (tuple)**:

#    * `paper_lengths` (dict)
#    * `long_papers` (list, długość >= 20)

# Następnie:

# * wywołaj tę funkcję
# * przypisz wynik do dwóch zmiennych
# * wydrukuj wynik dokładnie jak wcześniej

# ### Zasady

# * Jedna pętla `for` **wewnątrz funkcji**
# * Zero kodu powielonego
# * Funkcja **musi coś zwracać**, nie tylko drukować

# Pisz kod.
#_____________________________________________________________________________________________

papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]


def analyze_papers(papers):
    paper_lengths = {}
    long_papers = []
    for title in papers:
        length = len(title)
        paper_lengths[title] = length
        if length >= 20:
            long_papers.append(title)
        
    return paper_lengths, long_papers

paper_lengths, long_papers = analyze_papers(papers)

print(f"Paper lengths: {paper_lengths}")
print(f"Long papers: {long_papers}")
