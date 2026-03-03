import sys
import papers_io


papers = [
    "Attention Is All You Need",
    "GANs in Action",
    "A Survey on Transformers"
]

if sys.argv[1] == "load":
    print(papers_io.load_papers_from_json(sys.argv[2]))
elif sys.argv[1] == "save":
    papers_io.save_papers_to_json(papers, sys.argv[2])
    print(f"Saved papers to {sys.argv[2]}")
