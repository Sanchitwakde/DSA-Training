<<<<<<< HEAD
# num = int(input("Enter you mobile number: "))
num = str(input("Enter your mobile number: "))
# num = str("9877655432")

if num.isdigit():
    if len(num)==10:
        if num.startswith("9"):
            print("num is valid ")
        else:
            print("not valid")
else:
    print("not valid")
=======
# num = int(input("Enter you mobile number: "))
num = input("Enter your mobile number: ")
count = 0
s = str(num)
if s.isdigit():
    if len(s)==10:
        if s.startswith(6,7,8):
            print("num is valid ")
        else:
            print("not valid")
>>>>>>> f3c44600feff1c1c97f79fd3702729c39fef3c3d
