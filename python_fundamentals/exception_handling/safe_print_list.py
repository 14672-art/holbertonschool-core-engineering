#!/usr/bin/env python3
"""
Module pour afficher une liste de manière sécurisée.
"""


def safe_print_list(my_list=[], x=0):
    """
    Affiche x éléments d'une liste sans utiliser len().

    Args:
        my_list (list): La liste contenant n'importe quel type d'éléments.
        x (int): Le nombre d'éléments à afficher.

    Returns:
        int: Le nombre réel d'éléments affichés.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
