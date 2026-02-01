import sys
from fetch_titles import fetch_papers
import json


# n
if len(sys.argv) < 2:
    print("USAGE:")
    print("python3 app.py <query>")
    sys.exit(1)
else:
    query = sys.argv[1]



papers = fetch_papers(query)

data = {"papers": papers}

with open("papers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


print(f'Fetched {len(papers)} papers for query "{query}"')
print("Saved to papers.json")
