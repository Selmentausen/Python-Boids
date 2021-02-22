class Settings:
    def __init__(self):
        # Display settings
        self.screen_size = self.screen_width, self.screen_height = (800, 600)
        self.FPS = 60

        # Boid settings
        self.boid_velocity = 30
