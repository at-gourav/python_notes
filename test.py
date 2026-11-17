class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    def __str__(self):
        return f"radius : {self.radius} \ncolor : {self.color} "
    def _repr__(self):
        return f"{self.radius} \n {self.color} "

    


    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius


clsobj = Circle()
clsobj.radius = 10

print(clsobj)