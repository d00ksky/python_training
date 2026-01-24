import sys
import papers_io


papers = [
    "Attention Is All You Need",
    "GANs in Action",
    "A Survey on Transformers"
]
USAGE = """Usage:
python app.py save <filepath>
python app.py load <filepath>
python app.py stats <filepath>
python app.py add <filepath> "<title>"
"""

def print_usage_and_exit():
    print(USAGE)
    sys.exit(1)

def load_papers_or_exit(filepath):
    try:
        return papers_io.load_papers_from_json(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        sys.exit(1)

def cmd_load(filepath):
    print(load_papers_or_exit(filepath))
    
def cmd_save(filepath):
    papers_io.save_papers_to_json(papers, filepath)
    print(f"Saved papers to {filepath}")
    
def cmd_stats(filepath):
    loaded_papers = load_papers_or_exit(filepath)
    total_papers, long_papers = papers_io.paper_count(loaded_papers)
    print(f"Total papers: {total_papers}")
    print(f"Long papers: {long_papers}")
    
def cmd_add(filepath, title):
    loaded_papers = load_papers_or_exit(filepath)
    loaded_papers.append(title)
    papers_io.save_papers_to_json(loaded_papers, filepath)
    print(f"Added: {title}")

if len(sys.argv) < 2:
    print_usage_and_exit()
    
command = sys.argv[1]


if command in ('load', 'save', 'stats'):
    if len(sys.argv) != 3:
        print_usage_and_exit()
        
elif command == "add":
    if len(sys.argv) != 4:
        print_usage_and_exit()
else:
    print(f"Unknown command: {command}")
    print_usage_and_exit()
    

filepath = sys.argv[2]
title = sys.argv[3] if command == "add" else None

COMMANDS = {
    "save": cmd_save,
    "load": cmd_load,
    "stats": cmd_stats,
}


handler = COMMANDS.get(command)

if handler:
    handler(filepath)
elif handler == "add":
    title = sys.argv[3]
    cmd_add(filepath, title)
    sys.exit(0)
else:
    print(f"Unknown command: {command}")
    print_usage_and_exit()
    
