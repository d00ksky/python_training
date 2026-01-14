#_____________________________________________________________________________________________________ 
# ## Exercise 2: Jedna pętla, więcej myślenia

# Teraz robimy **to samo**, ale **lepiej**.

# ### Zadanie

# Napisz kod, który:

# 1. Na podstawie `papers`:

#    * tworzy `titles_upper`
#    * tworzy `long_titles`

# 2. Używa **tylko jednej pętli `for`**

# 3. Na końcu drukuje:

# ```text
# Total papers: X
# Long titles: Y
# ```

# ### Zasady

# * Jedna pętla. Druga = fail.
# * Zero liczników ręcznych.
# * Czytelne nazwy zmiennych.
# * Bez list comprehensions. Jeszcze nie teraz.

# Wklej kod.
#_____________________________________________________________________________________________________   

papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]
titles_upper = []
long_titles = []


for title in papers:
    titles_upper.append(title.upper())
    if len(title) > 20:
        long_titles.append(title)
        
print(f"Total papers: {len(papers)} \nLong titles: {len(long_titles)}")