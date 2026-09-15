#!/usr/bin/env python3
"""Module pour récupérer un élément d'une liste de manière sécurisée."""


def element_at(my_list, idx):
    """Renvoie l'élément à l'index `idx` ou None si l'index est invalide."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
