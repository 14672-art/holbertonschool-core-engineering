#!/usr/bin/env python3
"""Module pour remplacer un élément dans une liste."""


def replace_in_list(my_list, idx, element):
    """Remplace l'élément à la position idx si l'index est valide."""
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
