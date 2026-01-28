import urllib.request
import xml.etree.cElementTree as ET
import json
import sys

# n
if len(sys.argv) < 2:
    print("USAGE:")
    print("python3 fetch_titles.py <query>")
    sys.exit(1)
else:
    query = sys.argv[1]




def fetch_papers(query, max_results=5):
    URL = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"

    with urllib.request.urlopen(URL) as response:
        xml_bytes = response.read()

    xml_text = xml_bytes.decode("utf-8")

    ns = {"a": "http://www.w3.org/2005/Atom"}

    root = ET.fromstring(xml_text)
    #print(root)

    entries = root.findall("a:entry", ns)
    #print(entries)
    papers = []

    for entry in entries:
        title = entry.find("a:title", ns).text.strip()
        title_id = entry.find("a:id", ns).text.strip()
        authors = []
        for author in entry.findall("a:author", ns):
            name = author.find("a:name", ns).text.strip()
            authors.append(name)
        paper = {
            "id": title_id, 
            "title": title, 
            "authors": authors
            }
        papers.append(paper)
        
    return papers
        # print(f"  id: {title_id}")
        # print(f"  title: {title}")
        # print(f"  authors: {authors}")


#print(papers)
#print(ET.tostring(entries[0], encoding="unicode"))

#_____________________________________________________________________
fetch_papers(query)

data = {"papers": papers}

with open("papers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


with open("papers.json", encoding="utf-8") as f:
    loaded = json.load(f)


loaded_papers = loaded["papers"]
print(f"count of papers = {len(loaded_papers)}")
print(f"first paper title is = {loaded_papers[0]['title']}")

#_____________________________________________________________________


