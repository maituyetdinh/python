
import Subtract
import CalculateElectricity
import array as arr


CS1=int(input('Nhập chỉ số 1 : '))
CS2=int(input('Nhập chỉ số 2 : '))
GiaCu=[1549, 1600, 1858, 2340, 2615, 2701]
GiaMoi=[1687,1734,2014,2536,2834,2927]
Nhay=[50,50,100,100,100]

if CS2<=CS1:
    TongDienTT = int(Subtract.pheptru(CS2, CS1))
    print('Tổng điện tiêu thụ là: ', TongDienTT)
    print('Vui lòng nhập số hợp lệ để kiểm tra')
    exit(0)
else:

    TongDienTT=int(Subtract.pheptru(CS2,CS1))
    print('Tổng điện tiêu thụ là: ', TongDienTT)

Tong1= CalculateElectricity.TinhTienDien(TongDienTT,Nhay,GiaCu)
print('Tổng tiền mức giá cũ :', Tong1)
Tong2= CalculateElectricity.TinhTienDien(TongDienTT,Nhay,GiaMoi)
print('Tổng tiền mức giá mới :', Tong2)

print('Mức phí chênh lệch là :', Subtract.pheptru(Tong2, Tong1))
TiLeTang = (Tong2 / Tong1)
print('Tỉ lệ tăng : ', TiLeTang, '%')
print('Sài nhiều trả càng nhiều. Tiết kiệm điện là tiết kiệm tiền nha bà con.')

