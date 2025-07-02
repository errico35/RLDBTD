# utils/__init__.py

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Expose resource‐loading helpers:
from .resource_loader import load_image, load_sound, load_font, load_json, ResourceLoader

__all__ = [
    "load_image",
    "load_sound",
    "load_font",
    "load_json",
    "ResourceLoader",
]
