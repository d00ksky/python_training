from fetch_titles import fetch_papers

example_list = [
    "  deep   learning  ",
    "",
    "quantum    computing",
    " ai ",
    "   "
]


# n

def normalize_titles(titles: list[str]) -> list[str]:
    res = []
    for title in titles:
        new_title = title.strip().capitalize()
        new_title_after_space = " ".join(new_title.split())
        if new_title_after_space:
            res.append(new_title_after_space)
        
    return res




def get_normalized_titles(query: str) -> list[str]:
    papers = fetch_papers(query)
    titles = [paper["title"] for paper in papers]
    return normalize_titles(titles)

    






result = get_normalized_titles("transform")
print(result)