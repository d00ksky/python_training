#_______________________________________________________________________________________
# ## Next task: Exercise 12 (final boss for today): “append”

# Add a new command:

# ```bash
# python app.py add <filepath> "<title>"
# ```

# Behavior:

# * load papers from `<filepath>` (file must exist)
# * append the new title to the list
# * save back to the same file
# * print:

# ```text
# Added: <title>
# ```

# ### Rules

# * Reuse your existing load/save functions.
# * Don’t rewrite JSON handling in `app.py`.
# * Minimal code, no libraries, no overengineering.

# Write the updated `app.py` only.
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

        
