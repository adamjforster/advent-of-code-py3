class Submarine:
    x = 0
    y = 0
    aim = 0
    
    def __init__(self):
        with open('input.txt', 'r') as f:
            self.instructions = [(line.split(' ')[0], int(line.split(' ')[1])) for line in f]

    def up(self, amount):
        self.aim -= amount
    
    def down(self, amount):
        self.aim += amount
    
    def forward(self, amount):
        self.x += amount
        self.y += self.aim * amount

    def sail(self):
        for direction, amount in self.instructions:
            getattr(self, direction)(amount)
            
        print(self.x * self.y)

    
submarine = Submarine()
submarine.sail()
