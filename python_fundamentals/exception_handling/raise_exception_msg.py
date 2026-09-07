#!/usr/bin/env python3
"""
Module pour lever une exception NameError avec un message personnalisé.
"""


def raise_exception_msg(message=""):
    """
    Lève une exception NameError avec un message d'erreur spécifique.

    Args:
        message (str): Le message transmis avec l'exception.
    """
    raise NameError(message)
