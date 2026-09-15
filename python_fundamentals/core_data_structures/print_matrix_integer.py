#!/usr/bin/env python3
"""Module pour afficher une matrice d'entiers."""


def print_matrix_integer(matrix=[[]]):
    """Affiche une matrice d'entiers, ligne par ligne."""
    for row in matrix:
        print(" ".join("{:d}".format(elem) for elem in row))
