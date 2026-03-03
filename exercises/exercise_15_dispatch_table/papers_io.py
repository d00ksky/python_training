
#__________________________________________________________________
# ## Phase 4 – Exercise 15: Dispatch table (kill the if/elif monster)

# Goal: Replace the big `if/elif` command handling with a **dict of command → function**. Same behavior, cleaner structure.

# ### Requirements

# 1. Keep your helpers:

# * `print_usage_and_exit()`
# * `load_papers_or_exit(filepath)`

# 2. Create one function per command:

# * `cmd_save(filepath)`
# * `cmd_load(filepath)`
# * `cmd_stats(filepath)`
# * `cmd_add(filepath, title)`

# Each function should do exactly what the command currently does.

# 3. Create a dispatch dict, something like:

# ```python
# COMMANDS = {
#     "save": cmd_save,
#     "load": cmd_load,
#     "stats": cmd_stats,
# }
# ```

# `add` is special because it needs `title`. You can handle it in one of two acceptable ways:

# * **Option A:** don’t put `add` in the dict, keep a small `if command == "add": ...` branch
# * **Option B:** put `add` in the dict but dispatch with a lambda that passes title

# Pick whichever keeps the code clearer. Clarity wins.

# 4. Behavior must stay the same:

# * usage rules
# * file-not-found behavior
# * outputs

# ### Rules

# * Don’t touch `papers_io.py`
# * Don’t add libraries
# * Don’t overabstract

# ### Hint (minimal, because you’re ready)

# After validation, do:

# ```python
# handler = COMMANDS.get(command)
# if handler is None:
#     print(f"Unknown command: {command}")
#     print_usage_and_exit()
# handler(filepath)
# ```

# For `add`, either special-case it or pass `title`.

# ---

# Paste your refactored `app.py`.

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

        
