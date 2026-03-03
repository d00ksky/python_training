No mercy then.

## Welcome to Day 3. Here is your next exercise: **Exercise 18 – Parse arXiv XML and extract titles**

You already fetched the raw response. Now you’ll extract actual data like a grown-up.

### Goal

Fetch the same arXiv API URL and print the **titles** of the returned papers, **one per line**.

### URL (hardcoded for now)

```text
http://export.arxiv.org/api/query?search_query=all:transformer&start=0&max_results=5
```

### Requirements

1. Use **standard library only**:

   * `urllib.request`
   * `xml.etree.ElementTree` (ElementTree)

2. Parse the XML and extract:

   * every `<entry>`
   * inside each entry, the `<title>`

3. Print titles like:

```text
1. Title here
2. Another title
...
```

### Important detail (this is where humans suffer)

The arXiv response uses **namespaces**. That means naïve `find("entry")` usually returns nothing.

Hint for namespace handling (don’t ignore it):

```python
ns = {"a": "http://www.w3.org/2005/Atom"}
root.findall("a:entry", ns)
```

Similarly:

```python
entry.find("a:title", ns)
```

### Output rules

* Strip whitespace in titles (`.strip()`)
* Print exactly 5 titles (because max_results=5)

---

Paste your `fetch_titles.py` (or whatever you name it) code.
