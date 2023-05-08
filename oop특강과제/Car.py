class car():
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = 0
        
    def accelerate(self, accel):
        self.speed += accel
        print(self.speed)
    
    def brake(self, accel):
        self.speed -= accel
        if self.speed < 0:
            self.speed = 0
        print(self.speed)
            
    def get_speed(self):
        return self.speed
    
