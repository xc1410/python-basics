#1
def list_info(nums):
    a=(len(nums))
    b=(sum(nums))
    c=(max(nums))
    return a,b,c
length, total, largest = list_info([3,33,3445,211,1])
print(f"长度 {length}，总和 {total}，最大值 {largest}")
print(list_info([3,33,3445,211,1]))
print(list_info([323,363,34845,2101,19,56]))
#2
def print_config(config):
    for key in config:
        print(f"{key}")
    for value in config.values():
        print(f"{value}")
    for key,value in config.items():
        print(f"{key}--{value}")
print_config({"lr": 0.01, "batch_size": 32, "epochs": 10})


#3
def filter_students(students, line):
    names=[]
    for i in students:
        if i["scores"]>line:
            names.append(i["name"])
    return names
info = [{"name":"a","scores":87}, {"name":"b","scores":62}, {"name":"c","scores":91}]
print(filter_students(info, 85))   # ['a', 'c']
print(filter_students(info, 60))   # ['a', 'b', 'c']
