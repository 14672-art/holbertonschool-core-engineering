#!/usr/bin/env python3
"""Module qui définit la classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré.

        Args:
            size (int): La taille du côté (par défaut 0).
            position (tuple): Les coordonnées du carré (par défaut (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Récupère la taille du carré.

        Returns:
            int: La taille actuelle du côté.
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

    @property
    def position(self):
        """Récupère la position du carré.

        Returns:
            tuple: La position actuelle (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré après validation.

        Args:
            value (tuple): La nouvelle position du carré.

        Raises:
            TypeError: Si la position n'est pas un tuple de 2 entiers >= 0.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or value[0] < 0 or
                not isinstance(value[1], int) or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Calcule et renvoie la surface actuelle du carré.

        Returns:
            int: La surface du carré (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré dans stdout avec # et la position."""
        print(self.__str__())

    def __str__(self):
        """Renvoie la représentation sous forme de chaîne de caractères."""
        if self.__size == 0:
            return ""

        res = []
        for _ in range(self.__position[1]):
            res.append("")

        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)
