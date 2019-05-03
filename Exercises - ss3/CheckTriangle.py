def kiemtratamgiac(a,b,c):
    if a<0 or b<0 or c<0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        print('Đây không phải là tam giác')
    else:
        return True



