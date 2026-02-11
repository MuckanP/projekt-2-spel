from object import Block, Spike

class Level:
    def__init__(self, filename):
        self.blocks = []
        self.spikes = []
        self.load_level(filename)
        
    def load_level(self, filename):
        self.blocks.clear()
        self.spikes.clear()
    
    with open(filename, 'r') as file:
        level_map = [line.strip for line in file.readlines()]
        
    