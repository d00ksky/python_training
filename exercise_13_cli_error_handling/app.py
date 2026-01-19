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

if len(sys.argv) < 2:
    print(USAGE)
    sys.exit(1)
    
command = sys.argv[1]

if command in ('load', 'save', 'stats'):
    if len(sys.argv) != 3:
        print(USAGE)
        sys.exit(1)
elif command == "add":
    if len(sys.argv) != 4:
        print(USAGE)
        sys.exit(1)
else:
    print(f"Unknown command: {command}")
    print(USAGE)
    sys.exit(1)
    
        
filepath = sys.argv[2]


if command == "load":
    print(papers_io.load_papers_from_json(filepath))
elif command == "save":
    papers_io.save_papers_to_json(papers, filepath)
    print(f"Saved papers to {filepath}")
elif command == "stats":
    loaded_papers = papers_io.load_papers_from_json(filepath)
    total_papers, long_papers = papers_io.paper_count(loaded_papers)
    print(f"Total papers: {total_papers}")
    print(f"Long papers: {long_papers}")
elif command == "add":
    loaded_papers = papers_io.load_papers_from_json(filepath)
    loaded_papers.append(sys.argv[3])
    papers_io.save_papers_to_json(loaded_papers, filepath)
    print(f"Added: {sys.argv[3]}")

