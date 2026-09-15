#!/usr/bin/env python3
"""Module d'addition de deux tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Additionne les deux premiers éléments de deux tuples."""
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
