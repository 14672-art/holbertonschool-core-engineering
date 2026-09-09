#!/usr/bin/env python3
"""Module qui définit la classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise un carré.

        Args:
            size (int): La taille du côté (par défaut 0).
        """
        self.size = size

    @property
    def size(self):
        """Réfère ou définit la taille du carré.

        Returns:
            int: La taille actuelle du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré après validation.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et renvoie la surface actuelle du carré.

        Returns:
            int: La surface du carré (size * size).
        """
        return self.__size ** 2
