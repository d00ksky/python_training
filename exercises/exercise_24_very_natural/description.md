Następny krok (Exercise 24 – bardzo naturalny)
Teraz robimy coś, co od razu uprości kod:
Cel
Wyciągnąć całą logikę pobierania i parsowania do funkcji:
def fetch_papers(query, max_results=5):
    ...
    return papers
Dzięki temu:
CLI będzie cienkie
logika testowalna
gotowe pod prawdziwą arXiv app
To jest pierwszy architektoniczny krok, nie techniczny.
Jak skończysz 24:
wklej tylko definicję funkcji
resztę pominiemy
Jedziesz bardzo równo.