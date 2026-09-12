#1
def find_max(a):
    b=a[0]
    for i in a:
        if b<i:
            b=i
    return b
#2
def char_count(a):
    b={}
    for c in a:
        b[c]=b.get(c,0)+1
    return b
#3
def reverse_list(a):
    b=[]
    c=len(a)
    for i in range(c):
        b=b.append(a[c-1-i])
    return b 
    
