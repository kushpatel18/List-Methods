n=int(input("Enter the size of list: "))
l=[0]*n

for i in range(n):
    l[i]=int(input())

target=int(input("Enter target value: "))
temp=0
for i in range(n):
    if l[i]==target:
        temp=i










# if l[i]<target and i>temp:
#     temp2=l[i]
#     l[i]=l[i-1]
#     l[temp]=temp2
#     l[temp+1]=target



print(l)
