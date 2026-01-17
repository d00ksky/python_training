# Mini-zadanie zamykające próg (8a → 8b)
# Zrób jedno krótkie ćwiczenie, bez funkcji:
#
# Utwórz data z listą papers
# Zapisz ją do papers.json
# 
# W tym samym pliku:
#   wczytaj papers.json
#   print() wczytaną listę
# 
# Jak zobaczysz, że:
#   zapisujesz
#   czytasz
#   dane się zgadzają
# 
# to próg JSON + pliki masz zaliczony.
# Wklej kod.

import json

papers = [
    "Attention Is All You Need",
    "GANs in Action",
    "A Survey on Transformers"
]

data = {"papers": papers}

with open("papers.json", "w") as f:
    json.dump(data, f)

with open("papers.json") as f:
    loaded_data = json.load(f)

print(loaded_data)
