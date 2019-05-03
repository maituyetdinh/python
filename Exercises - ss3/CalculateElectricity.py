def TinhTienDien(TongDienTT,Nhay,GiaCu):
    TongTien1=0
    #TongDienTT=int(Subtract.pheptru(CS2,CS1))
    for x in range(0,len(Nhay)+1):
            if x == len(Nhay):
                TongTien1 += TongDienTT * GiaCu[x]
                break
            if TongDienTT-Nhay[x]>=0:
                TongTien1+=Nhay[x]*GiaCu[x]
               # TongTien2 += Nhay[x] * GiaCu[x]
                TongDienTT=TongDienTT-Nhay[x]
            else:
                TongTien1+=TongDienTT*GiaCu[x]
                #TongTien2 += TongDienTT * GiaCu[x]
                break
    return TongTien1

#print('Phải trả cũ: ', TinhTienDien(125,Nhay,GiaCu) )
#print('Phải trả mới: ', TinhTienDien(125,Nhay,GiaMoi) )