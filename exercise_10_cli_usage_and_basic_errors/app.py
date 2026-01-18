import sys
import papers_io


papers = [
    "Attention Is All You Need",
    "GANs in Action",
    "A Survey on Transformers"
]


if len(sys.argv) < 3:
    print("Usage:")
    print("  python app.py save <filepath>")
    print("  python app.py load <filepath>")
    sys.exit(1)



if sys.argv[1] == "load":
    print(papers_io.load_papers_from_json(sys.argv[2]))
elif sys.argv[1] == "save":
    papers_io.save_papers_to_json(papers, sys.argv[2])
    print(f"Saved papers to {sys.argv[2]}")
else:
    print(f"Unknown command: <{sys.argv[1]}>")
    sys.exit(1)
