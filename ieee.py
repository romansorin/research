import types, Book, Journal, Article

info = {
    'authors': ['R. Sorin', 'R. M. Sorin', 'dsdsd']
}

def generate_citation(type, info):
    if type == types.JOURNAL:
        return Journal(info).cite()
    elif type == types.BOOK:
        return Book(info).cite()
    elif type == types.ARTICLE:
        return Article(info).cite()


print(generate_citation('journal', info))
