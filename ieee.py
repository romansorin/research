
types = {
    'JOURNAL': 'journal',
    'BOOK': 'book',
    'ARTICLE': 'article'
}

info = {
    'authors': ['R. Sorin', 'R. M. Sorin', 'dsdsd']
}


class Reference:
    def __init__(self, info):
        self.info = info
        self.reference = []

    def cite(self):
        for author in self.info['authors']:
            self.reference.append(author)
        return self.reference


class Journal(Reference):
    def __init__(self, info):
        self.info = info
        self.reference = []

    def cite(self):
        for author in self.info['authors']:
            self.reference.append(author)
        return self.reference


class Book(Reference):
    def __init__(self, info):
        self.info = info
        self.reference = []

    def cite(self):
        for author in self.info['authors']:
            self.reference.append(author)
        return self.reference


class Article(Reference):
    def __init__(self, info):
        self.info = info
        self.reference = []

    def cite(self):
        for author in self.info['authors']:
            self.reference.append(author)
        return self.reference


def generate_citation(type, info):
    if type == types['JOURNAL']:
        return Journal(info).cite()
    elif type == types['BOOK']:
        return Book(info).cite()
    elif type == types['ARTICLE']:
        return Article(info).cite()


print(generate_citation('journal'))
