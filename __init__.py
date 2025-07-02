# engine/__init__.py

import logging

# Set up a null handler so library users won't get "No handler found" warnings
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Expose core classes at the package level for convenient imports:
from .settings import COLORS, ASSET_PATHS, DATA_PATHS


__all__ = [
    "settings"
    "utils",
    "engine",
    "screens",
    "actors",
    "data"
]
