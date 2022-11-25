import random
import pygame

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer


class PowerUpManager:
    def _init_(self):
        self.power_ups = []
        self.when_appears = 0

    def update(self, score, game_speed, player):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            joao = random.randint(0, 1)
            if joao == 0:
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Hammer())

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if self.power_ups == 1:
                    player.shield = True
                    player.hammer = False

                else:
                    player.hammer = True
                    player.shield = False

                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)   
                             

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
        