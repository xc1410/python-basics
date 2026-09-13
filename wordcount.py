text = "the quick brown fox jumps over the lazy dog the fox runs"
print(text)

b=[]
b=text.split()
print(len(b))

a={}
for c in b:
    if c not in a:
      a[c]=0
    a[c]+=1

c=[]
for key, value in a.items():
    d=(key,value)
    c.append(d)

e=sorted(c,key= lambda x: x[1],reverse=True)
for n in e[:10]:
    print(n) 

