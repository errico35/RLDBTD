"""
Main game entry point and core game loop.
"""
from .imports import *
from .settings import *
from .utils.resource_loader import ResourceLoader
from .screens.menu_screen import MenuScreen
from .screens.world_map_screen import WorldMapScreen
from .screens.level_screen import LevelScreen

class GameStateManager:
    """
    Manages game states and transitions between different screens.
    """
    
    def __init__(self):
        self.states: Dict[GameState, object] = {}
        self.current_state: Optional[GameState] = None
        self.running = True
        self.transition_data = {}  # Data to pass between states
        
        # Performance tracking
        self.frame_count = 0
        self.fps_timer = 0
        self.current_fps = 0
        
    def add_state(self, state_name: GameState, state_object):
        """Add a new state to the manager."""
        self.states[state_name] = state_object
        
    def switch_state(self, state_name: GameState, transition_data: dict = None):
        """
        Switch to a different state.
        
        Args:
            state_name: The state to switch to
            transition_data: Optional data to pass to the new state
        """
        if state_name in self.states:
            # Call exit method on current state if it exists
            if self.current_state and hasattr(self.states[self.current_state], 'on_exit'):
                self.states[self.current_state].on_exit()
            
            self.current_state = state_name
            self.transition_data = transition_data or {}
            
            # Call enter method on new state if it exists
            if hasattr(self.states[self.current_state], 'on_enter'):
                self.states[self.current_state].on_enter(self.transition_data)
                
            print(f"Switched to state: {state_name}")
        else:
            print(f"Warning: State {state_name} not found!")
    
    def handle_events(self, events):
        """Pass events to current state."""
        if self.current_state and self.current_state in self.states:
            current_state_obj = self.states[self.current_state]
            if hasattr(current_state_obj, 'handle_events'):
                current_state_obj.handle_events(events)
    
    def update(self, dt: float):
        """Update current state."""
        if self.current_state and self.current_state in self.states:
            current_state_obj = self.states[self.current_state]
            if hasattr(current_state_obj, 'update'):
                current_state_obj.update(dt)
    
    def draw(self, surface: pygame.Surface):
        """Draw current state."""
        if self.current_state and self.current_state in self.states:
            current_state_obj = self.states[self.current_state]
            if hasattr(current_state_obj, 'draw'):
                current_state_obj.draw(surface)
    
    def quit(self):
        """Signal to quit the game."""
        self.running = False
        print("Game quit requested")
    
    def update_fps(self, dt: float):
        """Update FPS counter."""
        self.frame_count += 1
        self.fps_timer += dt
        
        if self.fps_timer >= 1.0:  # Update every second
            self.current_fps = self.frame_count
            self.frame_count = 0
            self.fps_timer = 0
    
    def get_fps(self) -> int:
        """Get current FPS."""
        return self.current_fps

class Game:
    """
    Main game class that handles initialization and the core game loop.
    """
    
    def __init__(self):
        self.screen: Optional[pygame.Surface] = None
        self.clock: Optional[pygame.time.Clock] = None
        self.state_manager: Optional[GameStateManager] = None
        self.resource_loader: Optional[ResourceLoader] = None
        self.running = False
        
        # Debug info
        self.debug_font: Optional[pygame.font.Font] = None
        
    def initialize(self) -> bool:
        """
        Initialize Pygame and game systems.
        
        Returns:
            True if initialization successful, False otherwise
        """
        try:
            # Initialize Pygame
            pygame.init()
            pygame.mixer.init(
                frequency=22050,
                size=-16,
                channels=AUDIO_SETTINGS['channels'],
                buffer=AUDIO_SETTINGS['buffer_size']
            )
            
            # Create display
            flags = 0
            if FULLSCREEN:
                flags |= pygame.FULLSCREEN
            if VSYNC:
                flags |= pygame.DOUBLEBUF
                
            self.screen = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT), 
                flags
            )
            pygame.display.set_caption(TITLE)
            
            # Create clock
            self.clock = pygame.time.Clock()
            
            # Initialize resource loader
            self.resource_loader = ResourceLoader()
            
            # Initialize debug font
            self.debug_font = pygame.font.Font(None, UI_SETTINGS['font_size_small'])
            
            # Initialize state manager
            self.state_manager = GameStateManager()
            
            # Create and add all states
            self._initialize_states()
            
            # Set initial state
            self.state_manager.switch_state(GameState.MENU)
            
            self.running = True
            print("Game initialization successful")
            return True
            
        except Exception as e:
            print(f"Game initialization failed: {e}")
            return False
    
    def _initialize_states(self):
        """Initialize all game states."""
        try:
            # Create state objects
            menu_screen = MenuScreen(self.state_manager)
            world_map_screen = WorldMapScreen(self.state_manager)
            level_screen = LevelScreen(self.state_manager, "example_level")
            
            # Add states to manager
            self.state_manager.add_state(GameState.MENU, menu_screen)
            self.state_manager.add_state(GameState.WORLD_MAP, world_map_screen)
            self.state_manager.add_state(GameState.LEVEL, level_screen)
            
            print("All game states initialized")
            
        except Exception as e:
            print(f"Failed to initialize states: {e}")
            raise
    
    def handle_events(self):
        """Handle pygame events."""
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                self.state_manager.quit()
            
            elif event.type == pygame.KEYDOWN:
                # Global key handlers
                if event.key == pygame.K_F11:
                    # Toggle fullscreen
                    self._toggle_fullscreen()
                elif event.key == pygame.K_F3:
                    # Toggle debug info
                    DEBUG['show_fps'] = not DEBUG['show_fps']
        
        # Pass events to state manager
        self.state_manager.handle_events(events)
    
    def update(self, dt: float):
        """Update game logic."""
        # Update state manager
        self.state_manager.update(dt)
        
        # Update FPS counter
        if DEBUG['show_fps']:
            self.state_manager.update_fps(dt)
        
        # Check if state manager wants to quit
        if not self.state_manager.running:
            self.running = False
    
    def draw(self):
        """Render the game."""
        # Clear screen
        self.screen.fill(COLORS['BACKGROUND'])
        
        # Draw current state
        self.state_manager.draw(self.screen)
        
        # Draw debug info
        if DEBUG['show_fps']:
            self._draw_debug_info()
        
        # Update display
        pygame.display.flip()
    
    def _draw_debug_info(self):
        """Draw debug information overlay."""
        if not self.debug_font:
            return
            
        debug_info = [
            f"FPS: {self.state_manager.get_fps()}",
            f"State: {self.state_manager.current_state}",
        ]
        
        y_offset = 10
        for info in debug_info:
            text_surface = self.debug_font.render(info, True, COLORS['WHITE'])
            self.screen.blit(text_surface, (10, y_offset))
            y_offset += 20
    
    def _toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        global FULLSCREEN
        FULLSCREEN = not FULLSCREEN
        
        flags = 0
        if FULLSCREEN:
            flags |= pygame.FULLSCREEN
        if VSYNC:
            flags |= pygame.DOUBLEBUF
            
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), 
            flags
        )
        print(f"Fullscreen: {FULLSCREEN}")
    
    def run(self):
        """Main game loop."""
        if not self.initialize():
            return
        
        print("Starting main game loop")
        last_time = time.time()
        
        try:
            while self.running:
                # Calculate delta time
                current_time = time.time()
                dt = current_time - last_time
                last_time = current_time
                
                # Limit delta time to prevent large jumps
                dt = min(dt, 1.0 / 30.0)  # Cap at 30 FPS minimum
                
                # Handle events
                self.handle_events()
                
                # Update game logic
                self.update(dt)
                
                # Render
                self.draw()
                
                # Control frame rate
                self.clock.tick(FPS)
                
        except Exception as e:
            print(f"Error in game loop: {e}")
            import traceback
            traceback.print_exc()
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources and quit."""
        print("Cleaning up...")
        
        # Clear resource cache
        if self.resource_loader:
            self.resource_loader.clear_cache()
        
        # Quit Pygame
        pygame.mixer.quit()
        pygame.quit()
        
        print("Cleanup complete")

def main():
    """Entry point for the game."""
    print(f"Starting {TITLE}")
    print(f"Python version: {sys.version}")
    print(f"Pygame version: {pygame.version.ver}")
    
    # Create and run game
    game = Game()
    game.run()
    
    print("Game ended")
    sys.exit(0)

if __name__ == "__main__":
    main()