#_____________________________________________________________________________
# ## Phase 2 – Exercise 6: Funkcje wołające funkcje

# Teraz sprawdzimy, czy **myślisz w klockach**, a nie w jednym długim skrypcie.

# ### Zadanie

# Masz już funkcję:

# ```python
# filter_papers_by_word(papers, word)
# ```

# Napisz **drugą funkcję**:

# ```python
# def analyze_and_filter_papers(papers, word):
#     ...
# ```

# która:

# 1. Wywołuje `filter_papers_by_word`
# 2. Dla **przefiltrowanych tytułów**:

#    * tworzy słownik `paper_lengths`
#    * tworzy listę `long_papers` (>= 20)
# 3. Zwraca **krotkę (tuple)**:

# ```python
# (filtered_papers, paper_lengths, long_papers)
# ```

# ### Na końcu

# * wywołaj `analyze_and_filter_papers`
# * rozpakuj wynik do trzech zmiennych
# * wydrukuj wszystko w czytelnej formie

# ### Zasady

# * `filter_papers_by_word` **nie może być zmieniana**
# * Jedna pętla `for` w `analyze_and_filter_papers`
# * Zero duplikowania logiki
# * Funkcje **zwracają**, nie drukują

# To jest już **mini-architektura**.
# Pisz kod.
#_____________________________________________________________________________

papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]

def filter_papers_by_word(papers, word):
    filtered_words = []
    for title in papers:
        if word.lower() in title.lower():
            filtered_words.append(title)
    return filtered_words

def analyze_and_filter_papers(papers, word):
    paper_lengths = {}
    long_papers = []
    filtered_papers = filter_papers_by_word(papers, word)
    for title in filtered_papers:
        length = len(title)
        paper_lengths[title] = length
        if length >= 20:
            long_papers.append(title)
    return filtered_papers, paper_lengths, long_papers

filtered_papers, paper_lengths, long_papers = analyze_and_filter_papers(papers, "survey")

print(f"filtered papers = {filtered_papers}")
print(f"paper lengths = {paper_lengths}")
print(f"long papers = {long_papers}")

