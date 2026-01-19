
#__________________________________________________________________
# ## Phase 4 – Exercise 14: Reduce duplication, clarify intent

# ### What we’re fixing

# Your `app.py` currently has:

# * repeated `try/except FileNotFoundError` blocks
# * repeated printing of usage
# * CLI logic mixed with “how to fail nicely”

# It works, but it’s noisy. Noise kills scale.

# We are **not** changing behavior.
# We are only changing **shape**.

# ---

# ## Task

# ### Step 1: Add two small helper functions to `app.py`

# 1. **`print_usage_and_exit()`**

#    * prints `USAGE`
#    * calls `sys.exit(1)`

# 2. **`load_papers_or_exit(filepath)`**

#    * tries to load papers using `papers_io.load_papers_from_json`
#    * if file is missing:

#      * prints `File not found: <filepath>`
#      * exits with code `1`
#    * otherwise returns the papers list

# These functions live in **`app.py`**, not in `papers_io.py`.

# ---

# ### Step 2: Refactor `app.py` to use them

# After refactor:

# * there should be **no duplicated `try/except FileNotFoundError`**
# * usage printing should happen via **one function**
# * main command logic should read almost like pseudocode

# Example of the *style* we’re aiming for (not exact code):

# ```python
# papers = load_papers_or_exit(filepath)
# total, long = papers_io.paper_count(papers)
# ```

# Clean. Obvious. No defensive clutter everywhere.

# ---

# ## Rules

# * Do **not** change program behavior
# * Do **not** touch `papers_io.py`
# * No new features
# * No clever abstractions
# * If it feels “too simple”, you’re doing it right

# ---

# ## Why this matters

# This is the phase where:

# * juniors keep stacking `if/try/except`
# * seniors start extracting intent

# You’re learning to **shape code**, not just make it run.
#__________________________________________________________________


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

        
