#!/usr/bin/env python3
"""Module qui définit la classe Rectangle."""


class Rectangle:
    """Représente un rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise un nouveau rectangle.

        Args:
            width (int): La largeur du rectangle (par défaut 0).
            height (int): La hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle.

        Returns:
            int: La largeur actuelle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle avec validation.

        Args:
            value (int): La nouvelle largeur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle avec validation.

        Args:
            value (int): La nouvelle hauteur.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et renvoie la surface du rectangle.

        Returns:
            int: La surface du rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calcule et renvoie le périmètre du rectangle.

        Returns:
            int: Le périmètre du rectangle ou 0 si un côté vaut 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
