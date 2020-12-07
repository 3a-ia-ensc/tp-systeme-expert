# -*- coding: utf-8 -*-

__author__ = "Simon Audrix and Gabriel Nativel-Fontaine"
__credits__ = ["Simon Audrix", "Gabriel Nativel-Fontaine"]
__copyright__ = "Copyright 2020, TP représentation des connaissances"
__license__ = "WTFPL"
__version__ = "1.0.0"
__email__ = "gnativ910e@ensc.fr"
__status__ = "Development"

from src.Fact import *


class AkiNN:
    def __init__(self):
        self.facts = set()
        self.givenFacts = set()
        self.rules = []

    def addFact(self, text):
        self.facts.append(Fact(text))

    def addRule(self, rule):
        """
        :param rule:
        :return:
        """
        for f in rule.facts:
            self.facts.add(f)

        self.facts.add(rule.product_fact)

        self.rules.append(rule)

    def _getRulesForFact(self, fact):
        """
        :param fact:
        :return:
        """
        l = []
        for r in self.rules:
            if fact == r.product_fact:
                l.append(r)

        return l

    def _ask(self, fact):
        """
        :param fact:
        :return:
        """
        print(f'Est-ce que {fact} ?')

    def _propagateRule(self, rule, given_facts, who='terminal'):
        new_fact = None
        loop = False

        print(rule)
        if rule.is_fulfilled(given_facts):
            new_fact = rule.product_fact
            rule.active = False
            loop = True
            print(f"Admit new fact {new_fact}")

        return loop, new_fact

    def _reactivateRules(self):
        for r in self.rules:
            r.active = True

    def ForwardChaining(self, given_facts):
        """
        :param who:
        :param given_facts:
        :return:
        """
        self._reactivateRules()
        result = []
        bib = []

        loop = True
        while loop:
            loop = False
            for rule in self.rules:
                if rule.active:
                    status, fact = self._propagateRule(rule, given_facts)
                    loop |= status
                    if status:
                        given_facts.append(fact)
                        if fact.type == 'terminal':
                            result.append(fact)
                        if fact.type == 'article':
                            bib.append(fact)

        return result, bib

    def BackwardChaining(self, fact, given_facts):
        """
        :param fact:
        :param given_facts:
        :return:
        """
        print("BC for fact " + str(fact))
        for rule in self._getRulesForFact(fact):
            print(rule)
            for pre in rule.facts:
                if pre not in given_facts:
                    rulespre = self._getRulesForFact(pre)
                    if not rulespre:  # no rules conclude on it. This is an askable fact
                        self._ask(pre)
                        return True
                    else:
                        return self.BackwardChaining(pre)
