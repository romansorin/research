#!/usr/bin/env python
# coding: utf-8

from Book import Book
from Journal import Journal
from Article import Article

JOURNAL = 'journal'
BOOK = 'book'
ARTICLE = 'article'

# General reference info:
# Author’s name listed as first initial of first name, then full last.
# • Title of article, patent, conference paper, etc., in quotation marks.
# • Title of journal or book in italics.

info = {
    'authors': ['R. Sorin', 'R. M. Sorin', 'dsdsd'],
    'article': 'Neural Networks',
    'journal': 'Algorithms Designed'
}


def generate_citation(type, info):
    if type == JOURNAL:
        return Journal(info).cite()
    elif type == BOOK:
        return Book(info).cite()
    elif type == ARTICLE:
        return Article(info).cite()


print(generate_citation('journal', info))
