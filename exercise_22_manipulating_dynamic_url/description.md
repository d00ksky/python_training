exercise_21_json_dump_and_readCo dalej: Exercise 22 — pierwszy krok w stronę arXiv app

Teraz robimy coś, co:
NIE dodaje nowej technologii
ALE zmienia sposób użycia

Exercise 22 – parametryzuj zapytanie
Cel:
zamiast hardcoded:
all:transformer
mieć zmienną:

query = "transformer"

I zbudować URL dynamicznie:

query = "transformer"
URL = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"

Na razie:
bez CLI
bez sys.argv
po prostu zmienna na górze pliku
Test
Zmień:
query = "graph"
i zobacz, że JSON się zmienia.