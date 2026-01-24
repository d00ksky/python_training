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
    title_el = entry.find("a:title", ns)
    title_id_el = entry.find("a:id", ns)
    title = title_el.text.strip()
    title_id = title_id_el.text.strip()
    print(f"{i}: id = {title_id} title = {title}")

    
#print(ET.tostring(entries[0], encoding="unicode"))
