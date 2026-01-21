
#__________________________________________________________________

# Phase 5 – Exercise 17 (HTTP basics)

# Czas na zewnętrzny świat: pobieranie danych przez HTTP.
# Zadanie

# Napisz plik fetch_arxiv.py, który:

# Pobiera dane z URL (na razie hardcoded):
# http://export.arxiv.org/api/query?search_query=all:transformer&start=0&max_results=5

# Wypisuje:
# status code
# długość odpowiedzi (liczba znaków)
# pierwsze 300 znaków odpowiedzi

# Zasady
# Użyj tylko standardowej biblioteki: urllib.request
# Bez requests (jeszcze)
# Bez parsowania XML (jeszcze)
# Jeśli request się nie uda, po prostu wypisz wyjątek i zakończ (na razie)

# Hint
# W standard library:
# urllib.request.urlopen(url) zwraca response
# response.read() daje bytes
# bytes zamieniasz na string przez .decode("utf-8")

# Wklej kod fetch_arxiv.py jak zrobisz.
# I tak: HTTP to będzie moment, w którym “rzeczywistość” zacznie się wtrącać. Idealnie.
#__________________________________________________________________


import json


def save_papers_to_json(papers, filepath):
    data = {'papers': papers}
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
        
def load_papers_from_json(filepath):
    with open(filepath) as f:
        read_data = json.load(f)
    return read_data["papers"]
    
def paper_count(papers):
    long_count = 0
    for title in papers:
        if len(title) >= 20:
            long_count += 1
    return len(papers), long_count

        
