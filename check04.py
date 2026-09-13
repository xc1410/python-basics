class Rect:
    def __init__(self,width,high):
        self.width=width
        self.high=high
    def area(self):
        return self.width*self.high
    def perimeter(self):
        return 2*(self.width+self.high)
    def show(self):
        print(f"该矩形的面积是{self.area()}，周长是{self.perimeter()}")

r1=Rect(10,12)
r2=Rect(4,20)
r1.show()
r2.show()