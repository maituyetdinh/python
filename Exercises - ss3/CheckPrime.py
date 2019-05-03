a=int(input('Nhập số cần kiểm tra: '))
def Prime(x):
    i=2
    while True:
        đếm = x % i
        if x==i:
            print('Số', x, 'là SNT')
            break
        if đếm==0:
            print('Số' , x , 'không phải SNT')
            break
        else:
            i+=1
            continue
    return x
Prime(a)


