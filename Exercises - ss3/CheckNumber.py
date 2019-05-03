#-----Kiểm tra số vừa nhập-----

#x=int(input('Nhập số cần kiểm tra : '))
def kiemtraso(x):
    while True:
        if x<0:
            print('Số vừa nhập không phải số nguyên dương')
            print('Vui lòng nhập lại số cần kiểm tra')
            x=int(input('Nhập số khác cần kiểm tra : '))
            continue
    return x

#-------------------------------
def pheptru(a,b):
    return(a-b)
