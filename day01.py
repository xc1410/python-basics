#1.1
xc=21
ckx=2005.042
kc="follow"
inkx=True
print(xc,ckx,kc,inkx)
#1.12
kx=10
xc=11
print(kx,xc)
kx,xc=xc,kx
print(kx,xc)
#1.3
epoch=100
loss=0.001
学习率=0.0001
准确率="99%"
耗时=36
print(f"第{epoch}轮，loss={loss}，学习率={学习率}，准确率={准确率}，耗时={耗时}")
#2.1
score = 96
if score>=90:
    print("youxiu")
elif score >= 75:
    print("lianghao")
elif score >=60:
    print("jige")
else :
    print("bujige")
#2.2
a=0
if a>0:
    print("zhengshu")
elif a==0:
    print("ling")
else:
    print("fushu")
#2.3
b=2000
if b%4==0 and b%100!=0 or b%100==0 and b%400==0:
    print("runshu")
else:
    print("bushi")
#2.4
models=["chat","gpt","claude"]
if "lllma" in models:
    print("lllma在modles")
else:
    print("buzai1")
#3.1
for i in range(5):
 print (i)
#3.2
a=[0,1,2,3,4,5]
for i in a:
    print(i)
#3.3
i=10
while i>=1:
    print(i)
    i-=1
#3.4
a=list(range(1,1000))
for i in a:
 if i>100:
    break
 print(i)
#3.5
for i in range(10):
    if i%3==0:
        continue
    print(i)
#3.6
total=0
for i in range(101):

    total+=i
print(total)

summ=0
#
i=1
while  i <=100:
 summ +=i
 i+=1
print(summ)
#4.1
def is_even(n):
    if n%2==0:
        return(True)
    else:
       return(False)
n=0
print(is_even(n))
#4.2
def sum_to(n=100):
    a=0
    for i in range(n+1):
     
       
       a+=i

    
    return(a)
n=10
print(sum_to(n=100))
#4.3
def bigger(a,b):
    if a>=b:
        return(a)
    else:
        return(b)

print(bigger(10,10))
#4.4
def print_multiples(n,k=3):
    for i in range(1,n+1):
        if i%k==0:
           print(i)
      
print(print_multiples(n,5))
#4.5
def train(epochs=10, lr=0.001, batch_size=32):
    print(f"epochs={epochs}, lr={lr}, batch_size={batch_size}")

train(lr=0.1)
train(0,1,1)
train(epochs=1, lr=1, batch_size=2)





        
