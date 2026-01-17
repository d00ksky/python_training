import json


papers = [
    "Attention Is All You Need",
    "GANs in Action",
    "A Survey on Transformers"
]

def save_papers_to_json(papers, filepath):
    data = {'papers': papers}
    with open(filepath, 'w') as f:
        json.dump(data, f)
        
save_papers_to_json(papers, "papers2.json")

def load_papers_from_json(filepath):
    with open(filepath) as f:
        read_data = json.load(f)
    return read_data["papers"]

print(load_papers_from_json('papers2.json'))