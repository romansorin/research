import Reference

class Book(Reference):
    def __init__(self, info):
        self.info = info
        self.reference = []

    def cite(self):
        for author in self.info['authors']:
            self.reference.append(author)
        return self.reference
