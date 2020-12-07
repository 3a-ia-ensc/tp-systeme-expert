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

    def _propagateRule(self, rule, given_facts):
        empty = True
        ret = False
        for pre in rule.facts:
            print("evaluating ", pre)
            if pre != given_facts:
                empty = False
                break
        if empty:
            print("Propagating rule " + str(rule.pre) + " => " + str(rule.post))
            for post in rule.product_fact:
                if post != given_facts:
                    if self.verb: print("Adding " + post + " as a new fact")
                    given_facts(post)
                    ret = True  # At least one fact has been added
            rule.active = False
        return ret

    def ForwardChaining(self, given_facts):
        """
        :param given_facts:
        :return:
        """
        loop = True  # True if any fact has been added
        while loop:
            loop = False
            for rule in self.rules:
                if rule.active:
                    loop |= self._propagateRule(rule, given_facts)

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
