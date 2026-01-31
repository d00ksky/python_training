import sys


# n
if len(sys.argv) < 2:
    print("USAGE:")
    print("python3 fetch_titles.py <query>")
    sys.exit(1)
else:
    query = sys.argv[1]
