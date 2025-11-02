name = input()
age = input()
print(f"Xin chào {name}, bạn {age} tuổi!")

a, b = map(int, input().split())
print(a+b, a-b, a*b, a/b)

a, b = map(int, input().split())
print((a+b)*2, a*b)

a = float(input())
print(a*2*3.14, a*a*3.14)

a = float(input())
print(a*(9/5)+32)

#
a = int(input())
print("chan" if a%2==0 else "le")

a = int(input())
print("duong" if a>0 else "am" if a<0 else "0")

a = float(input())
print("Yeu" if a<5 else "Trung binh" if a<7 else "Kha" if a<8.5 else "Gioi")

a = input().split()
print(max(a))

a = int(input())
print("Nam nhuan" if a%4==0 and a%100!=0 else "Nam khong nhuan")

#
for a in range(1, 11):
    print(a)

a = int(input())
sum = 0
for i in range(a+1): 
    sum+=i
print(sum)

for a in range(1, 11):
    print(a*9)

a = int(input())
for i in range(a):
    a*=i
print("1" if a==0 else a)

#15

#
a = input().split()
sum = 0
for i in a:
    sum+=float(a)
print(sum, max(a))

a = input().split()
b = ""
for i in a:
    if len(a)>len(b):
        b = a
print(b)

a = input().split()
print(i for i in a if int(i)>=8)

#
a = input()
count=0
for i in a:
    if i=="a":
        count+=1
print(count)

#20



 
