with open("test.txt","w",encoding="utf-8") as f:
    f.write("xunlianwancheng\n")
with open("test.txt","r",encoding="utf-8") as f:
    content=f.read()
print(content)
#dedup
def dedup(nums):
    result=[]
    for n in nums:
        if n not in result:
            result.append(n)
    return result

print(dedup([3, 1, 3, 2, 1]))   # 期望 [3, 1, 2]
print(dedup([3, 1, 2]))         # 期望 [3, 1, 2]  ← 证伪组

def dedup1(nums):
    result={}
    final_result=[]
    for n in nums:
        if n not in result:
            result[n]=1

    for key in result:
        final_result.append(key)
    return final_result


print(dedup1([3, 1, 3, 2, 1]))   # 期望 [3, 1, 2]
print(dedup1([3, 1, 2]))         # 期望 [3, 1, 2]  ← 证伪组
#MyData
class MyData:
    def __init__(self,d): 
        self.data=d

    def __len__(self):
        return len(self.data)
    def __getitem__(self, i):
        return self.data[i]
        

d = MyData([10, 20, 30, 40])

print(len(d))      # 期望 4
print(d[2])        # 期望 30
print(d[-1])       # 期望 40
for x in d:
    print(x)       # 期望 10 20 30 40