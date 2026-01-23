#Below as redoing exercise 18

import urllib.request
import xml.etree.cElementTree as ET

URL = "http://export.arxiv.org/api/query?search_query=all:transformer&start=0&max_results=5"


with urllib.request.urlopen(URL) as response:
    xml_bytes = response.read()

xml_text = xml_bytes.decode("utf-8")

root = ET.fromstring(xml_text)

ns = {"a": "http://www.w3.org/2005/Atom"}

entries = root.findall("a:entry", ns)

for i, entry in enumerate(entries[:5], start=1):
    title_el = entry.find("a:title", ns)
    title = title_el.text.strip()
    print(f"{i}: {title}")

#for child in root:
#    print(child.tag)
