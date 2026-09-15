#!/usr/bin/env python3
"""Module pour trouver la clé ayant la plus grande valeur."""


def best_score(a_dictionary):
    """Renvoie la clé avec la plus grande valeur entière dans a_dictionary."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
