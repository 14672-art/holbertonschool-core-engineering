#!/usr/bin/env python3
"""
Module pour afficher uniquement les entiers d'une liste.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Affiche les x premiers éléments d'une liste s'ils sont des entiers.

    Args:
        my_list (list): La liste d'éléments.
        x (int): Le nombre d'éléments à examiner.

    Returns:
        int: Le nombre réel d'entiers imprimés.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
