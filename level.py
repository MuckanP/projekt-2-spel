import pygame
from object import Block, Spike
from settings import TILE_SIZE, GRAY, RED

class Level:
    def __init__(self, filename):
        self.filename = filename
        self.blocks = []
        self.spikes = []
        self.level_width = 0
        self.level_height = 0
        self.load_level(filename)

    def load_level(self, filename):
        self.blocks.clear()
        self.spikes.clear()

        with open(filename, "r") as file:
            level_map = [line.rstrip("\n") for line in file.readlines()]

        max_cols = max(len(row) for row in level_map) if level_map else 0
        self.level_width = max_cols * TILE_SIZE
        self.level_height = len(level_map) * TILE_SIZE

        for row_index, row in enumerate(level_map):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if tile == "#":
                    self.blocks.append(Block(x, y, TILE_SIZE, TILE_SIZE))
                elif tile == "X":
                    self.spikes.append(Spike(x, y, TILE_SIZE, TILE_SIZE))

    def reset(self):
        self.load_level(self.filename)

    def update(self):
        pass  # Objects are static; camera handles all movement

    def draw(self, screen, camera_x, camera_y):
        for block in self.blocks:
            draw_rect = block.rect.move(-camera_x, -camera_y)
            pygame.draw.rect(screen, GRAY, draw_rect)

        for spike in self.spikes:
            draw_rect = spike.rect.move(-camera_x, -camera_y)
            sx = spike.rect.x - camera_x
            sy = spike.rect.y - camera_y
            sw = spike.rect.width
            sh = spike.rect.height
            points = [
                (sx + sw // 2, sy),
                (sx, sy + sh),
                (sx + sw, sy + sh),
            ]
            pygame.draw.polygon(screen, RED, points)