#_______________________________________________________________________________________
# Here is your next exercise: Exercise 13

# ### Goal

# Add **basic file error handling** to your CLI so it doesn’t crash when the JSON file doesn’t exist.

# ### Requirement

# For commands that **read** a file:

# * `load`
# * `stats`
# * `add`

# If the filepath does **not** exist, print **exactly**:

# ```text
# File not found: <filepath>
# ```

# …and exit with code `1` (use `sys.exit(1)`).

# ### Rules

# * Update **`app.py` only**
# * Use `try/except`
# * Catch **only** `FileNotFoundError`
# * Do **not** catch broad exceptions (`except Exception:` is lazy and bad)
# * Keep `papers_io.py` unchanged

# ### Hint (one, because I’m generous today)

# Wrap the call that reads the file. Example pattern:

# ```python
# try:
#     papers = papers_io.load_papers_from_json(filepath)
# except FileNotFoundError:
#     print(f"File not found: {filepath}")
#     sys.exit(1)
# ```

# Do this only for the read commands. `save` should still create/overwrite the file normally.

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

        
