while True:
    n = int(input("Nhập 1 số nguyên dương"))
    dem=0
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
    if dem==2:
        print(n,"là số nguyên tố")
    else:
        print(n,"không là số nguyên tố")
    hoi=str(input("tiếp không?(c/k):"))
    if hoi is "k":
        break
print("BYE!")
