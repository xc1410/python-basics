# ---- 1. 最大值 ----
def find_max(nums):
    b=nums[0]
    for c in nums:
        if b<c:
            b=c
    return b

print(find_max([3, 1, 4, 1, 5]))   # 期望 5
print(find_max([-2, -7, -3]))      # 期望 -2
# ---- 2. 所有偶数 ----
def find_even(nums):
    b=[]
    for c in nums:
        if c%2==0:
            b.append(c)
    return b


print(find_even([1,2,3,4]))   # 期望 [2,4]
print(find_even([1,3,5]))      # 期望 []

def find_even1(nums):
    b=[c for c in nums  if c%2==0]
    
    return b


print(find_even1([1,2,3,4]))   # 期望 [2,4]
print(find_even1([1,3,5]))      # 期望 []
# ---- 3. 字符计数 dict ----
def char_count(word):
    b={}
    for c in word:
        if c not in b:
            b[c]=0
        b[c]+=1
    return b
print(char_count("hello"))   # 期望l:2
print(char_count("aaa"))      # 期望 {a:3}
# ---- 4. 两个 list 的公共元素 ----
def the_same(a,b):
    c=[]
    for n in a:
        if n in b and n not in c:
            c.append(n)
    return c



print(the_same([1, 2, 3], [2, 3, 4]))    # 期望 [2, 3]
print(the_same([10, 20, 30], [20, 40]))  # 期望 [20]   ← 抓下标/值混淆
print(the_same([1, 1, 2], [1, 2]))       # 期望 [1, 2] ← 抓去重，新增
# ---- 5. 反转 ----
def contrast(nums):
    result=[]
    for i in range(len(nums)):
        result.append(nums[len(nums)-1-i])
    return result


print(contrast([1,2,3,4]))   
print(contrast([1,2,3]))      
# ---- 6. 1 到 n 求和 （for + while 两版）----
def summ(n):
    total=0
    for i in range(n+1):
        total+=i
    return total


print( summ(5))   # 期望 15
print( summ(1))      # 期望 1

def summ1(n):
    total=0
    i=0
    while i<=n:
        total+=i
        i+=1
    return total


print( summ1(5))   # 期望 15
print( summ1(1))      # 期望 1

# ---- 7. 找下标，找不到返回 -1 ----
def find_under(nums,target):
    for i in range(len(nums)):
        if target == nums[i]:
            return i
    return -1

print(find_under([1,2,3],2))   # 期望 1
print(find_under([1,2,3],9 ))      # 期望 -1
print(find_under([4,7,4],4))      # 期望 0
#8. dict 按 value 从大到小打印 key ----
def rank(a):
    b=sorted(a.items() ,key= lambda x:x[1],reverse=True)
    for key in b:
        print(key[0])

rank({"a":1,"b":5,"c":3})   
#Vector
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def sub(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def dot(self,other):
            return self.x*other.x+self.y*other.y
    def show(self):
            print(f"Vector({self.x},{self.y})")

v1 = Vector(1, 2)
v2 = Vector(3, 5)
v1.add(v2).show()   # 期望 (4, 7)
v1.sub(v2).show()   # 期望 (-2, -3)   ← 方向，9/14 的坑
print(v1.dot(v2))   # 期望 13
v1.show()           # 期望 (1, 2)     ← v1 没被改
#MyData
class MyData:
    def __init__(self,data,data1):
        self.data=data
        self.data1=data1
    def __len__(self):
        return len(self.data)
    def __getitem__(self,n):
        return self.data[n],self.data1[n]
d = MyData([10, 20, 30], [0, 1, 0])
print(len(d))    # 期望 3
print(d[2])      # 期望 (30, 0)      ← 测 d[2] 本身，不是 len(d[2])