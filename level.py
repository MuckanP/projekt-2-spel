from object import Block, Spike
from settings import Block, Spike

class Level:
    def __init__(self, filename): 
        self.blocks = []
        self.spikes = []
        self.load_level(filename)
        
    def load_level(self, filename):
        self.blocks.clear()
        self.spikes.clear()
        
        with open(filename, "r") as file: #ladda in level filen, se till att den läses in i rätt format
            level_map = [line.strip for line in file.readlines()]
        
        for row_index, row in enumerate(level_map):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if tile == "#":
                    self.blocks.append(Block(x, y, TILE_SIZE, TILE_SIZE))
                    
                elif tile == "^":
                    self.spikes.append(Spike(x, y, TILE_SIZE // 2, TILE_SIZE // 2))
                    
    def update(self, scroll_speed):
        for block in self.blocks:
            block.update(scroll_speed)
            
        for spike in self.spikes:
            spike.update(scroll_speed)
            
    def draw(self, screen):
        for block in self.blocks:
            block.draw(screen)
            
            for spike in self.spikes:
                spike.draw(screen)
                    
                