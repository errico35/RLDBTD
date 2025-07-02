# actors/__init__.py

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

# Expose actor classes:
from .player import Player
from .enemy  import Enemy
from .towers  import Tower
from .base_actor import BaseActor
from allied_units import AlliedUnit

# If you have a common BaseActor class, include it too:
# from .base_actor import BaseActor

__all__ = [
    "Player",
    "Enemy",
    "Tower",
    "BaseActor",
    "AlliedUnit"
]
