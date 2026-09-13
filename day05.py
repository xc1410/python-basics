#1
class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        print(f"我是一个{self.name}")
class Circle(Shape):
    def area(self):
        return 3.14
c = Circle("圆形")
c.describe()        # 我是一个圆形
print(c.area())     # 3.14
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
c = Circle(5)
print(c.area())     # 78.5
c.describe()        # ← 这行会崩
#2
# import torch.nn as nn
# class MyModel(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.player=nn.Linear(10,1)
#     def forward(self,x):
#         return self.player(x)
#3
def min_max(nums):
    min_v=nums[0]
    max_v=nums[0]
    for n in nums:
        if min_v>n:
            min_v=n
        if max_v<n:
            max_v=n
    return min_v,max_v
    

print(min_max([3, 1, 4, 1, 5]))        # (1, 5)
low, high = min_max([3, 1, 4, 1, 5])
print(low, high)                        # 1 5

    
