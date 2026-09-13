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

#1
def my_strip(s):
    left=0
    while left+1<=len(s) and s[left]==" ":
        left=left+1
    right=len(s)-1
    while right>=0 and s[right]==" ":
            right=right-1
    return s[left:right+1]

    
    

print(my_strip("   hello   "))       # hello
print(my_strip("  a b  "))           # a b      ← 中间那个空格要留着
print(my_strip("abc"))               # abc
print(my_strip("    "))              # 空字符串
#2
def my_split(a):
    result=[]
    word=""
    for c in a:
        if c!=" ":
            word=word+c
        else:
            if word !="":
                result.append(word)
                word=""
    if word !="":
        result.append(word)

    return result   
print(my_split("a b c"))          # ['a', 'b', 'c']
print(my_split("hello world"))    # ['hello', 'world']
print(my_split("a  b"))           # ['a', 'b']   ← 两个空格，不要空字符串

#3
def thesame(a,b):
    result=[]
    for n1 in a:
        if n1 in b and n1 not in result:
            result.append(n1)
    return result
a = [1, 2, 2, 3]
b = [2, 3, 4]

# 1. 用两层循环求交集
# 2. 用 set 求交集，对比行数
print(thesame(a,b))
print(thesame([10, 20, 30], [0, 1, 20]))   # 必须是 [20]

def thesame_set(a, b):
    s1=set(a)
    s2=set(b)
    result=s1 & s2
    return result
a = [1, 2, 2, 3]
b = [2, 3, 4]
print(thesame_set(a,b))


    
