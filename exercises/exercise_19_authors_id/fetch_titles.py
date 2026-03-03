import urllib.request
import xml.etree.cElementTree as ET

# n

URL = "http://export.arxiv.org/api/query?search_query=all:transformer&start=0&max_results=5"

with urllib.request.urlopen(URL) as response:
    xml_bytes = response.read()
    
xml_text = xml_bytes.decode("utf-8")

ns = {"a": "http://www.w3.org/2005/Atom"}

root = ET.fromstring(xml_text)
#print(root)

entries = root.findall("a:entry", ns)
#print(entries)

for i, entry in enumerate(entries[:5], start=1):
    title = entry.find("a:title", ns).text.strip()
    title_id = entry.find("a:id", ns).text.strip()
    authors = []
    for author in entry.findall("a:author", ns):
        name = author.find("a:name", ns).text.strip()
        authors.append(name)
    print(f"{i}:")
    print(f"  id: {title_id}")
    print(f"  title: {title}")
    print(f"  authors: {authors}")


    
#print(ET.tostring(entries[0], encoding="unicode"))
