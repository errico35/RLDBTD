# engine/__init__.py

import logging

# Set up a null handler so library users won't get "No handler found" warnings
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Expose core classes at the package level for convenient imports:
from .map_loader   import MapLoader, TileMap
from .deck_system  import Deck, Hand, Card
from .tower_defense import TowerManager, WaveManager, ProjectileManager
from .entity_manager import EntityManager

__all__ = [
    "MapLoader",
    "TileMap",
    "Deck",
    "Hand",
    "Card",
    "TowerManager",
    "WaveManager",
    "ProjectileManager",
    "EntityManager",
]
