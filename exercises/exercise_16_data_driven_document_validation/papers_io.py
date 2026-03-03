
#__________________________________________________________________

# ## Phase 4 – Exercise 16: Data-driven argument validation

# This is the last polish step before Phase 5.

# ### Goal

# Remove **all** hardcoded argument-count logic and replace it with data.

# ### Task

# Create a dict:

# ```python
# ARGS_REQUIRED = {
#     "save": 3,
#     "load": 3,
#     "stats": 3,
#     "add": 4,
# }
# ```

# Then validation becomes:

# 1. If `command` not in `ARGS_REQUIRED` → unknown + usage
# 2. If `len(sys.argv) != ARGS_REQUIRED[command]` → usage

# No `if command == ...` trees. One table, one rule.

# ### Rules

# * No behavior change
# * No new features
# * Validation happens **before** `filepath = sys.argv[2]`
# * Keep dispatch table as-is

# ### End state

# Your `main` logic should read almost like English:

# > get command → validate → dispatch

# Paste the updated `app.py` when done.

# After this:

# * Phase 4 is **complete**
# * Phase 5 starts (external data, APIs)
# * and the arXiv app stops being “soon” and starts being “next”

# Go.

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

        
