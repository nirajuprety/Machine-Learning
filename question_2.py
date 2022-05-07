import json
from operator import itemgetter


lib = {
    "book1": {"BookName": "TOC", "BookAuthor": "James Clear", "PublishedYear": 2019},
    "book2": {
        "BookName": "grammar",
        "BookAuthor": "Ram  Bahadur",
        "PublishedYear": 2016,
    },
    "book3": {"BookName": "DAA", "BookAuthor": "Hari Gopal", "PublishedYear": 2017},
    "book4": {
        "BookName": "DSA",
        "BookAuthor": "Madhav Kumar Nepal",
        "PublishedYear": 2004,
    },
    "book5": {"BookName": "SAD", "BookAuthor": "KP OLI", "PublishedYear": 2022},
    "book6": {"BookName": "web", "BookAuthor": "BALEN SHAH", "PublishedYear": 2020},
    "book7": {"BookName": "PHY", "BookAuthor": "MAILA", "PublishedYear": 2003},
    "book8": {"BookName": "MATHS", "BookAuthor": "GBOB", "PublishedYear": 2008},
    "book9": {"BookName": "DBMS", "BookAuthor": "Dhiraj K. JHA", "PublishedYear": 2012},
    "book10": {
        "BookName": "AI",
        "BookAuthor": "Mukesh Chaudary",
        "PublishedYear": 1999,
    },
}


def book_published_year(lib: dict) -> dict:
    """this function takes dictionary as an argument,
    saves the dictionary in json file and returns
    dictionary sorted by published year

    Args:
        lib(dict): dictionary of 10 books with
        their respective book name, book author  and
        published year

    Returns:
        dict: dictionary sorted by published year
    """
    print(type(lib))
    published_year = sorted(lib, key=itemgetter("PublishedYear"))
    with open("data.json", "w") as outfile:
        json.dump(published_year, outfile)
    return published_year


print(book_published_year(lib))
