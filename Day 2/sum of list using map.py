<<<<<<< HEAD
n = int(input("Enter size:"))
ele = 0
sum = 0
for i in range (n):
    eles = map(int,input("enter you element: ").split())
    ele.append(list(eles))

for x in range(len(ele)):
    sum = sum + ele[x]
=======
n = int(input("Enter size:"))
ele = 0
sum = 0
for i in range (n):
    eles = map(int,input("enter you element: ").split())
    ele.append(list(eles))

for x in range(len(ele)):
    sum = sum + ele[x]
>>>>>>> f3c44600feff1c1c97f79fd3702729c39fef3c3d
    print(sum)