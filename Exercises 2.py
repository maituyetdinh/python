#---------- Bài 1 ----------
print ('------ Bài tập 1 : Fizz / Buzz ------')
x=float(input('Nhập số : '))
print ('Bạn vừa nhập', x)
if x%3==0 and x%5==0:
    print (x, 'là FizzBuzz')
elif x%3==0:
    print(x, 'là Fizz')
elif x%5==0:
    print(x, 'là Buzz')
else:
    print('Opps')

#----------- Bài 2 -----------
print('----------- Bài tập 2 : In ***** ------')
row=int(input('nhập số dòng: '))
if row==5:
    print ('*')
    print ('**')
    print ('***')
    print ('****')
    print ('*****')
else: print('Không in *')


#----------- Bài 3 -----------
print('----------- Bài tập 3 : EVEN / ODD ------')
limit=int(input('nhập số giới hạn: '))
x=0
while x<=limit:
    if x%2==0:
        print(x, 'EVEN')
    else: print(x, 'ODD')
    x+= 1

#----------- Bài 4 -----------
print('----------- Bài tập 4 : tính điểm tốc độ ------')
#speed : 70< x<=75 =>1 ; 75 <=80 : 2 ; > 12 points, print: “License suspended”
x=int(input('Nhập tốc độ : '))
point=0
x=x-75
while x>=0:
    point+=1
    x=x-5
if point >=12:
    print('You have' , point, 'points. License suspended')
else : print('You have' , point, 'point(s). Go on!')

#nháp





