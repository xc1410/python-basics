class Cat:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def meow(self):
        print(f"{self.color}的{self.name}叫")

cat1=Cat("mimi","yellow")
cat2 = Cat("dahei", "black")
cat1.meow()
cat2.meow()

class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def show(self):
        print(f"{self.name}考了{self.score}分")
student1=Student("xc",520)
student2=Student("ckx",1314)
student1.show()
student2.show()        

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"Vector({self.x},{self.y})")
    def add(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def sub(self,other):
            return Vector(self.x-other.x,self.y-other.y)
    def dot(self,other):
        return self.x*other.x+self.y*other.y

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v1.show()              # Vector(1, 2)
v3 = v1.add(v2)
v3.show()              # Vector(4, 6)
v4 = v1.sub(v2)
v4.show()              # Vector(-2, -2)
print(v1.dot(v2))      # 11
v1.show()              # Vector(1, 2)
        

    
