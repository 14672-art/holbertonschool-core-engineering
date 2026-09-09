#!/usr/bin/env python3
"""Module qui définit la classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise un carré.

        Args:
            size (int): La taille du côté (par défaut 0).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcule et renvoie la surface actuelle du carré.

        Returns:
            int: La surface du carré (size * size).
        """
        return self.__size ** 2
