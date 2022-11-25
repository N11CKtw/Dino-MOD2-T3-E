from dino_runner.utils.constants import BIRD, BENTIVI
from dino_runner.components.obstacles.obstacle import Obstacle
from pygame import mixer
import time


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
   
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0

        bentivi_sound = mixer.Sound(BENTIVI)
        bentivi_sound.play()
        bentivi_sound.set_volume(0.05)
        time.sleep(0)
    