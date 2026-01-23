import urllib.request
import xml.etree.ElementTree


data = urllib.request.urlopen('http://export.arxiv.org/api/query?search_query=all:transformer&start=0&max_results=5')

status = data.getcode()

encoded_data = data.read()

decoded_data = encoded_data.decode("UTF-8")
data_length = len(decoded_data)
cut_data = decoded_data[:300]
print(f"status code = {status}")
print(f"data length is = {data_length}")
print(f"first 300 characters = {cut_data}")