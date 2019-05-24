"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Các hàm xử lý chuỗi : letter : isalpha() ; digit : isdigit() ; special : isalnum() ; space : isspace()
"""

print('Nhập chuỗi: ')
s = input('')
d = l = 0
for i in s:
    if i.isalpha():
        l = l+1
    elif i.isdigit():
        d += 1
    else:
        pass
print('The output should be:')
print('LETTERS : ', l)
print('DIGITS : ', d)

