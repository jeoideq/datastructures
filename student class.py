class Ball():
    def __init__(self,x,y,color,radius):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
    
    def display(self):
        print(self.x,self.y,self.color,self.radius)
        
shape=Ball(36,58,str("blue"),10)
shape.display()


