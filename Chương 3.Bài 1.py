print("Chương trình kiểm tra năm nhuận: ")

year=int(input("mời bạn nhập vào 1 năm: "))
if (year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
    print("Năm",year,"là năm nhuận")
else:
    print("Năm",year,"không nhuận")