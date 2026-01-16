#_______________________________________________________________________________
# ## Phase 2 – Exercise 5: Funkcje + logika

# ### Zadanie

# Napisz funkcję:

# ```python
# def filter_papers_by_word(papers, word):
#     ...
# ```

# która:

# * przyjmuje listę tytułów
# * przyjmuje jedno słowo (string)
# * zwraca **nową listę tytułów**, które zawierają to słowo
# * wyszukiwanie ma być **case-insensitive**

# Przykład:

# ```python
# filter_papers_by_word(papers, "survey")
# ```

# powinno zwrócić:

# ```python
# ["A Survey on Transformers"]
# ```

# ### Zasady

# * Jedna pętla
# * Bez list comprehensions
# * Bez modyfikowania oryginalnej listy
# * Funkcja **zwraca**, nie drukuje

# Pisz kod.
#_______________________________________________________________________________

papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]

def filter_papers_by_word(papers, word):
    filtered_words = []
    for title in papers:
        if word.lower() in title.lower():
            filtered_words.append(title)
    return filtered_words

print(filter_papers_by_word(papers, "survey"))
