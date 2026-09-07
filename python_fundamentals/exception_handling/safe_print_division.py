#!/usr/bin/env python3
"""
Module pour diviser deux entiers en toute sécurité.
"""


def safe_print_division(a, b):
    """
    Divise deux entiers et affiche le résultat dans un bloc finally.

    Args:
        a (int, float): Le numérateur.
        b (int, float): Le dénominateur.

    Returns:
        float or None: Le résultat de la division a / b, ou None si échec.
    """
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
