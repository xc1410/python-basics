#1
def filter_students(students,line):
    names=[]
    for s in students:
        if s["scores"]>line:
            names.append(s["name"])
    return names
#2
def find_index(nums,target):
    length=len(nums)
    for i in range(length):
        if nums[i]==target:
            return i
    return -1
#3
def line_(words):
    
    result=sorted(words.items(),key = lambda x: x[1],reverse=True)
    for key,value in result:
        print(key,value)
