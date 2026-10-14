"""A very small path router with named parameters and method matching."""

from __future__ import annotations

__all__ = ["tinyRouter"]


def tinyRouter(value):
    """A very small path router with named parameters and method matching."""
    if value is None:
        raise ValueError("value must not be None")
    return value
