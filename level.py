from object import Block, Spike
from settings import tile_size

class Level:
    def __init__(self, filename): 
        self.blocks = []
        self.spikes = []
        self.load_level(filename)
        
    def load_level(self, filename):
        self.blocks.clear()
        self.spikes.clear()
    
    with open(filename, "#") as file: #ladda in level filen, se till att den läses in i rätt format
        level_map = [line.strip for line in file.readlines()]
        
        for row_index, row in enumerate(level_map):
            for col_index, tile in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if tile == "#":
                    self.blocks.append(Block(x, y, tile_size, tile_size))
                elif tile == "^":
                    self.spikes.append(Spike(x, y, tile_size, tile_size))
                    
                