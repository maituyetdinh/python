import CheckTriangle

a=int(input('Nhập cạnh 1 : '))
b=int(input('Nhập cạnh 2 : '))
c=int(input('Nhập cạnh 3 : '))

def LoaiTamGiac():
    if CheckTriangle.kiemtratamgiac(a,b,c)==True:
        if a==b and b==c:
            print('Đây là tam giác đều')
        elif a==b or a==c or b==c:
            print('Đây là tam giác cân')
        elif a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b and a==b or a==c or b==c:
            print('Đây là tam giác vuông cân')
        elif a*a==b*b+c*c or b*b==a*a+c*c or c*c== a*a+b*b:
            print('Đây là tam giác vuông')
        else:
            print('Đây là tam giác thường')
    else:
        print('Hãy nhập lại các giá trị hợp lệ')
LoaiTamGiac()
