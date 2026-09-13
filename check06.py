#MyData
class MyData:
    def __init__(self,data):
        self.data=data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, i):
        return self.data[i]
#dedup1
def dedup1(nums):
    result={}
    final_result=[]
    for c in nums:
        if c not in result:
            result[c]=1
    for c in result:
        final_result.append(c)
    return final_result
d = MyData([10, 20, 30, 40])

print(len(d))      # 期望 4
print(d[2])        # 期望 30
print(d[-1])       # 期望 40
for x in d:
    print(x)       # 期望 10 20 30 40
print(dedup1([3, 1, 3, 2, 1]))   # 期望 [3, 1, 2]
print(dedup1([3, 1, 2]))         # 期望 [3, 1, 2]  ← 证伪组
#3
class MyData:
    def __init__(self,nums,names):
        self.nums=nums
        self.names=names
    def __len__(self):
        return len(self.nums)
    def __getitem__(self, i):
        return self.nums[i],self.names[i]
        

d = MyData([10, 20, 30], ["猫", "狗", "猫"])
print(d[1])        # 期望 (20, '狗')
print(len(d))     # 期望 3
for x in d:       # 期望三行元组
    print(x)