#____________________________________________________________________________________________________
#Welcome to Day 1. Here is your first exercise:
#We start painfully basic because that’s how you stop writing fragile nonsense later.
#### Exercise 1: Strings and lists, no tricks
#Write **Python code only**, no explanations, no comments.
##### Task
#
#1. Create a variable called `papers` that is a **list of strings** with exactly these values, in #this order:
#
#   * `"Attention Is All You Need"`
#   * `"GANs in Action"`
#   * `"A Survey on Transformers"`
#
#2. Create a variable called `titles_upper` that contains the **same titles**, but
#
#   * all letters uppercased
#   * order preserved
#
#3. Create a variable called `long_titles` that contains **only titles longer than 20 characters**.
#
#4. Print:
#
#   * the number of all papers
#   * the number of long titles
#
#### Rules
#
#* No hardcoding counts.
#* No copying strings manually for `titles_upper`.
#* No list literals except for the original `papers`.
#* Clean, readable code. If it looks like Stack Overflow vomit, I’ll call it out.
#
#Write the code directly below.
#____________________________________________________________________________________________________



papers = ["Attention Is All You Need", "GANs in Action", "A Survey on Transformers"]
titles_upper = []
long_titles = []



for word in papers:
    titles_upper.append(word.upper())
    
    
for word in papers:
    if len(word) > 20:
        long_titles.append(word)

print(f"there are {len(papers)} papers total and {len(long_titles)} long titles")
