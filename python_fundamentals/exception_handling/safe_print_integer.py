#!/usr/bin/env python3
"""
Module pour afficher un entier de manière sécurisée.
"""


def safe_print_integer(value):
    """
    Affiche un entier au format "{:d}".

    Args:
        value: La valeur à afficher (de n'importe quel type).

    Returns:
        bool: True si la valeur est un entier et a été affichée,
              False sinon.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
