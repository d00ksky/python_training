#_______________________________________________________________________________________
# Exercise 11 (next)
# We’ll add:
# one more command: stats
#
# reuse existing functions
#
# zero new I/O concepts
#
# Example goal:
# python app.py stats papers.json
# Output:
# Total papers: 3
# Long papers: 2
# This will force you to:
# reuse logic instead of rewriting
# think about where computations belong
# feel the beginnings of “application shape”
# But not right now. You just finished a solid block.
# Take a breath, sip your coffee, and when you’re ready, say:
# next task
# And we keep building.
#_______________________________________________________________________________________

import json


def save_papers_to_json(papers, filepath):
    data = {'papers': papers}
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
        
def load_papers_from_json(filepath):
    with open(filepath) as f:
        read_data = json.load(f)
    return read_data["papers"]
    
def paper_count(papers):
    long_count = 0
    for title in papers:
        if len(title) >= 20:
            long_count += 1
    return len(papers), long_count

        
