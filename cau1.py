name=input("Nhập tên của bạn : ")
print("Tên của bạn là : ",name)
n=int(input("Nhập một số : "))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print (d)