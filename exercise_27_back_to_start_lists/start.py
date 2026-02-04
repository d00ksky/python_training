

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




result = normalize_titles(example_list)
print(result)