import urllib.request
import xml.etree.cElementTree as ET

# n

URL = "http://export.arxiv.org/api/query?search_query=all:transformer&start=0&max_results=5"

with urllib.request.urlopen(URL) as response:
    xml_el = response.read()
    xml_text = xml_el.decode("utf-8")


ns = {"a" : "http://www.w3.org/2005/Atom"}
    
root = ET.fromstring(xml_text)

entry = root.findall("a:entry", ns)
    
print(entry)    
#print(ET.tostring(entries[0], encoding="unicode"))
