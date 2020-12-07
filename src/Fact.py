# -*- coding: utf-8 -*-

__author__ = "Simon Audrix and Gabriel Nativel-Fontaine"
__credits__ = ["Simon Audrix", "Gabriel Nativel-Fontaine"]
__copyright__ = "Copyright 2020, TP représentation des connaissances"
__license__ = "WTFPL"
__version__ = "1.0.0"
__email__ = "gnativ910e@ensc.fr"
__status__ = "Development"


def neg(fact):
    return -fact


class Article:
    def __init__(self, authors, name, year, url=None):
        self.authors = authors
        self.name = name
        self.year = year
        self.url = url

    def __repr__(self):
        return f'[Bibliographie] {self.name}, {self.authors} ({self.year})'


class Fact:
    def __init__(self, text, description=None, fact_type=None, negation=False):
        self.text = text
        self.description = description
        self.negation = negation

        if isinstance(description, Article):
            self.type = 'article'
        else:
            self.type = fact_type

    def copy(self):
        return Fact(self.text, self.description, self.negation)

    def __repr__(self):
        if self.negation:
            return '!' + self.text
        else:
            return self.text

    def __str__(self):
        return self.__repr__()

    def __neg__(self):
        neg_fact = self.copy()
        neg_fact.negation = not neg_fact.negation
        return neg_fact

    def __and__(self, other):
        if isinstance(other, Fact):
            return Rule(self, other)

            """elif isinstance(other, Rule):
                other.addFact(other)"""

        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Fact):
            return other.text == self.text and other.negation == self.negation

        return False

    def __hash__(self):
        return hash(self.text)


class Rule:
    def __init__(self, f1, f2=None):
        if f2 is None:
            self.facts = [f1]
        else:
            self.facts = [f1, f2]

        self.product_fact = None
        self.active = True

    @property
    def len(self):
        return len(self.facts)

    def addFact(self, fact):
        self.facts.append(fact)

    def copy(self):
        copy_rule = Rule(self.facts[0], self.facts[1])
        if len(self.facts) > 2:
            for i in range(2, len(self.facts)):
                copy_rule.addFact(self.facts[i])
        return copy_rule

    def give(self, fact):
        self.product_fact = fact
        return self

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        s = ''
        for f in self.facts:
            s += str(f) + ' & '

        return s[:-3] + ' => ' + str(self.product_fact)

    def __and__(self, other):
        if isinstance(other, Fact):
            new_rule = self.copy()
            new_rule.addFact(other)
            return new_rule

        elif isinstance(other, Rule):
            new_rule = self.copy()
            for f in other.facts:
                new_rule.addFact(f)

            return new_rule

        else:
            raise TypeError
