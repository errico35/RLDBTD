from ..imports import *
from ..engine.deck_system import Card

# screens/level_screen.py

from ..imports import *           # your common imports, e.g., pygame, typing, etc.
from ..engine.deck_system import Card
from ..engine.map_loader import MapLoader
from ..engine.tower_defense import TowerManager, WaveManager
from ..engine.entity_manager import EntityManager
from ..actors.player import Player


class UI:
    def __init__(self, font: pygame.font.Font):
        """
        Attributes initialized here:
          - self.font: pygame Font for all text
          - self.energy_display: position or surface for energy
          - self.health_display: for player health
          - self.wave_info: for current wave / enemies remaining
        """
        self.font = font
        self.energy = 0
        self.health = 0
        self.wave = 0
        self.enemies_remaining = 0

    def update(self, player: Player, wave_manager: WaveManager):
        """Update all tracked values from game state."""
        self.energy = player.energy
        self.health = player.health
        self.wave = wave_manager.current_wave
        self.enemies_remaining = wave_manager.enemies_left

    def draw(self, surface: pygame.Surface):
        """Render UI overlay (energy, health, wave info)."""
        # Energy
        energy_surf = self.font.render(f"Energy: {self.energy}", True, (255, 255, 0))
        surface.blit(energy_surf, (10, 10))

        # Health
        health_surf = self.font.render(f"Health: {self.health}", True, (255, 0, 0))
        surface.blit(health_surf, (10, 40))

        # Wave info
        wave_surf = self.font.render(f"Wave: {self.wave}", True, (0, 255, 255))
        surface.blit(wave_surf, (10, 70))

        # Enemies remaining
        remain_surf = self.font.render(f"Enemies: {self.enemies_remaining}", True, (255, 255, 255))
        surface.blit(remain_surf, (10, 100))

    def draw_card_preview(self, surface: pygame.Surface, card: Card, pos: tuple[int, int]):
        """Show a tooltip-like preview of the given card at `pos`."""
        # Background box
        w, h = 200, 120
        box = pygame.Rect(pos[0], pos[1], w, h)
        pygame.draw.rect(surface, (50, 50, 50), box)
        pygame.draw.rect(surface, (200, 200, 200), box, 2)

        # Card name
        name_surf = self.font.render(card.name, True, (255, 255, 255))
        surface.blit(name_surf, (pos[0] + 10, pos[1] + 10))

        # Card cost / description
        cost_surf = self.font.render(f"Cost: {card.cost}", True, (255, 255, 0))
        surface.blit(cost_surf, (pos[0] + 10, pos[1] + 40))

        desc_lines = card.description.split('\n')
        for i, line in enumerate(desc_lines):
            line_surf = self.font.render(line, True, (200, 200, 200))
            surface.blit(line_surf, (pos[0] + 10, pos[1] + 70 + i*20))


class LevelScreen:
    def __init__(self, state_manager, level_id: str, font: pygame.font.Font = pygame.font.get_default_font()):
        """
        Attributes:
          - state_manager: to push/pop screens
          - tile_map: instance of TileMap
          - player: Player instance
          - tower_manager: TowerManager
          - wave_manager: WaveManager
          - entity_manager: EntityManager
          - ui: UI overlay
          - camera: simple offset (x, y)
        """
        self.state_manager = state_manager
        self.tile_map = None
        self.player = None
        self.tower_manager = None
        self.wave_manager = None
        self.entity_manager = None
        self.ui = UI(font)
        self.camera = pygame.Vector2(0, 0)
        self.paused = False

        self.load_level(level_id)

    def load_level(self, level_id: str):
        """Load level data and initialize all subsystems."""
        path = f"/data/maps/{level_id}.json"
        self.tile_map = MapLoader.load_map(path)

        # Initialize core systems
        self.player = Player(start_pos=self.tile_map.spawn_points[0])
        self.tower_manager = TowerManager(self.tile_map)
        self.wave_manager = WaveManager(self.tile_map.spawn_points, level_id)
        self.entity_manager = EntityManager(self.tile_map, self.player)

    def handle_events(self, events: list[pygame.event.Event]):
        """Process input: movement, card plays, pause, etc."""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.pause_game()
            # TODO: mouse clicks on cards / towers
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     self.attempt_card_or_tower(event.pos)

    def update(self, dt: float):
        """Update all game systems if not paused."""
        if self.paused:
            return

        self.player.update(dt)
        self.wave_manager.update(dt)
        self.tower_manager.update(dt, self.entity_manager.enemies)
        self.entity_manager.update(dt)
        self.ui.update(self.player, self.wave_manager)

        if self.check_win_condition():
            self.on_level_complete()
        if self.check_lose_condition():
            self.on_level_failed()

    def draw(self, surface: pygame.Surface):
        """Render tilemap, entities, towers, UI, etc."""
        # apply camera offset
        cam_x, cam_y = -self.camera.x, -self.camera.y
        temp_surf = pygame.Surface((self.tile_map.width * self.tile_map.tile_size,
                                    self.tile_map.height * self.tile_map.tile_size))
        self.tile_map.draw(temp_surf)

        # draw towers & projectiles
        self.tower_manager.draw(temp_surf)
        self.entity_manager.draw(temp_surf)

        # blit world
        surface.blit(temp_surf, (cam_x, cam_y))

        # draw UI on top
        self.ui.draw(surface)

    def handle_card_play(self, card: Card, target_pos: tuple[int, int]):
        """Process a card play action (e.g., build a tower)."""
        if self.player.energy >= card.cost:
            self.player.energy -= card.cost
            self.tower_manager.place_tower(card.effect, target_pos)

    def handle_tower_placement(self, tower_type: str, pos: tuple[int, int]):
        """Direct tower placement (bypassing card)."""
        self.tower_manager.place_tower(tower_type, pos)

    def check_win_condition(self) -> bool:
        """Return True if all waves are done and no enemies remain."""
        return self.wave_manager.finished and not self.entity_manager.enemies

    def check_lose_condition(self) -> bool:
        """Return True if player's health is zero."""
        return self.player.health <= 0

    def on_level_complete(self):
        """Handle victory: notify state_manager, show screen, etc."""
        self.state_manager.push("level_complete")

    def on_level_failed(self):
        """Handle defeat: notify state_manager, show game-over, etc."""
        self.state_manager.push("level_failed")

    def pause_game(self):
        """Toggle pause state."""
        self.paused = not self.paused
