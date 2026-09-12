#1
scores=[10,9,8,7]
print(scores[0])#10
print(scores[-1])#7
print(scores[1:3])#9,8
print(scores[:3])#10,9,8
print(scores[2:])#8,7
scores.append(6)
print(scores[0])#10
print(scores[-1])#6
print(scores[1:3])#9,8
print(scores[:3])#10,9,8
print(scores[2:])#8,7,6
scores.remove(8)
print(scores[0])#10
print(scores[-1])#6
print(scores[1:3])#9,7
print(scores[:3])#10,9,7
print(scores[2:])#7,6
scores.pop()
print(scores[0])#10
print(scores[-1])#7
print(scores[1:3])#9,7
print(scores[:3])#10,9,7
print(scores[2:])#7
print(len(scores))
print(sum(scores))
print(max(scores))
print(6 in (scores))
for i in scores:
    print(i)
for i, value in enumerate(scores):
    print(f"{i}--{value}")
scores=[i*i for i in range(3)] 
print(scores)
scores=[i   for i in range(3) if i%2==0] 
print(scores)
scores=[i   for i in range(3)  if i>0] 
print(scores)
#1
a=[3,1,4,1,5,9]
print(len(a))
print(sum(a))
print(max(a))
#2
info={
    "name":"xc","age":"21","hobby":"football"}
for key,value in info.items():
    print(f"{key}={value}")
#3
scores = [88, 92, 79, 95, 63]
scores=[i for i in scores if i>80]
print(scores)
#1
info={
    "lr":0.01,"epchs":999,"batch_size":64
}
for key in info:
    print(f"{key}")
for value in info.values():
    print(f"{value}")
for key,value in info.items():
    print(f"{key}\{value}")
print(info.get("dropout",0))

info["dropout"]=0.2
print(info)
info["lr"]=0.1
print(info)
del info["lr"]
print(info)
print("lr" in info)
print(0.1 in info)
#2
students={
    "scores":[90,81,72,94,66],
    "names":["a","b","c","d","e"]
}
print(students["names"][2])

info=[
    {"name":"a","scores":87},
    {"name":"b","scores":90},
    {"name":"c","scores":68},
    {"name":"d","scores":45},
    {"name":"e","scores":100},
]
print(info[2]["name"])
for i in info:
    print(i["name"])
for i in info:
    if i["scores"]>85:
        print(i["name"])
#1
def find_max(a):
    b=a[0]
    for i in a:
        if b<i:
            b=i
    return(b)
print(find_max([3, 1, 4, 1, 5, 9]))   # 9
print(find_max([-2, -7, -1]))         # -1  ← 这个会坑到你
print(find_max([5]))                  # 5
#2
def count_even(a):
    b=0
    for i in a:
        if i%2==0:
            b+=1
    return(b)
print(count_even([1, 2, 3, 4, 5, 6]))   # 3
print(count_even([]))                   # 0
print(count_even([0, 7]))               # 1  ← 0 是偶数
#3
def char_count(s):
    b={}
    for c in s:
        if c in b:
            b[c]+=1
        else:
            b[c]=1
    return b


def char_count1(s):
    b={}
    for c in s:
        b[c]=b.get(c,0)+1
    return b

def char_count2(s):
    b={}
    for c in s:
        b.setdefault(c, 0)
        b[c]+=1
    return b
#4
def reverse_list(a):
    b=[]
    c=len(a)
    for i in range(c):
        b.append(a[c-1-i])
    return b
def reverse_list1(a):
    c=len(a)
    d=c//2
    for i in range(d):
        a[0+i],a[c-1-i]=a[c-1-i],a[0+i]
    return a
#5
def is_prime(a):
    if a<2:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                
                return False
    return True
            
print(is_prime(1))    # False  ← 1 不是质数
print(is_prime(2))    # True   ← 唯一的偶质数
print(is_prime(17))   # True
print(is_prime(25))   # False  ← 25 = 5×5，别漏了        










