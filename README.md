# IRS Assignment #2: Search Engines Algorithms 

### *Based on CS 106A Assignment #7: Bajillion Search Engine*

**Assignment: [link to assignment](./SearchEnginesAssignment2.pdf)**

*Student: **Vsevolod Pavlovskyi***

*Group: **KP21mp***

### Extra tasks implemented:

- Stop word elimination
- Word stemming
- CI test actions

### Instructions

#### Install dependencies:

`pip3 install -r requirements.txt`

---

#### Run doctests:

`python3 -m doctest -v common_elements.py searchengine.py extension.py`

---

#### Run server:

1. Run `python3 extension_server.py`
2. Navigate to http://localhost:8000 in a web-browser and enter search query in text input.

---

#### Run local search program:

`python3 searchengine.py DIR -s`

*Where DIR is **bbcnews** or **small***

