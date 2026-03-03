'''

⸻

🔹 Mikro-ćwiczenie (płynność dict + sortowanie)

Masz listę słowników:

papers = [
    {"title": "Paper A", "year": 2023, "citations": 15},
    {"title": "Paper B", "year": 2022, "citations": 40},
    {"title": "Paper C", "year": 2023, "citations": 5},
]

🎯 Cel

Zwrócić listę tytułów:
	•	tylko z roku 2023
	•	posortowanych malejąco po citations

Oczekiwany wynik

["Paper A", "Paper C"]

Wymagania
	•	nie modyfikuj oryginalnej listy
	•	jedna funkcja
	•	czytelne nazwy zmiennych

Hints
	1.	Najpierw przefiltruj po roku.
	2.	Użyj sorted(..., key=..., reverse=True).
	3.	Na końcu wyciągnij same tytuły.

⸻

Napisz funkcję. Nie kombinuj. Czysto i precyzyjnie.

'''



papers = [
    {"title": "Paper A", "year": 2023, "citations": 15},
    {"title": "Paper B", "year": 2022, "citations": 40},
    {"title": "Paper C", "year": 2023, "citations": 5},
]


def sort_2023_papers(papers):

    '''
    papers = []
    titles = []
    
    for paper in papers:
        year = paper["year"]
        if year == 2023:
            papers_2023.append(paper)
    papers_2023 = sorted(papers_2023, key=lambda paper: paper["citations"], reverse=True)
    for paper in papers_2023:
        title = paper["title"]
        titles.append(title)
    return titles
    
    '''
    papers_2023 = [paper for paper in papers if paper["year"] == 2023]
    papers_2023 = sorted(papers_2023, key=lambda paper: paper["citations"], reverse=True)
    titles = [paper["title"] for paper in papers_2023]
    return titles

result = sort_2023_papers(papers)
print(result)