'''
Thực hiện code lại hàm sau và cho biết ý nghĩa của nó
def enter_data():
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")
'''
# def enter_data(): # khai báo tên hàm
#     while True: # tạo vòng lặp while True
#         n = input("Nhập 1 số nguyên: ") # nhập số từ bàn phím
#         if n.isnumeric(): # điều kiện True or False nếu là số
#             n = int(n) # thực hiện ép kiểu từ str thành int
#             if n > 0: # điều kiện là số dương
#                 print("Đã nhập số dương")
#                 return n # lệnh thực thi khi hàm đúng điều kiện là số dương
#             else:
#                 print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
#         else:
#             print("Dữ liệu đã nhập không phải số nguyên")
# enter_data()

'''
Viết hàm
        def find_x(a_list, x)
trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
'''
# def find_x (a_list,x):
#     result = []
#     for i in range(len(a_list)):
#         if a_list[i] == x:
#             result.append(i)
#     if result:
#         return result
#     else:
#         return -1
#
# a_list = [1,2,3,4,5]
# x = 2
# find_x(a_list,x)
# print(find_x(a_list,x))

'''
Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy
'''
# # cách 1
# def nhap_so (n): # chú ý n chỉ được gọi trong hàm
#     if n <= 2:
#         return 1
#     else:
#         return nhap_so(n-1) + nhap_so(n-2)
# M = int(input('mời nhập số: ')) #
# print(nhap_so(M)) # M được khởi tạo và chứa các phép toán của hàm nhập số

#cách 2
'''Thuật toán được đưa ra là chúng ta sẽ dùng một mảng lưu lại các giá trị của hàm F(n), 
nếu như phần tử n có tồn tại giá trị trong mảng thì ta sử dụng luôn mà không cần tính toán lại giá trị.
Ngược lại thì tính F(n – 1) + F(n – 2) và lưu nó vào mảng, sau đó trả về giá trị vừa tính.

Chúng ta sẽ không gọi trực tiếp hàm tính số Fibonacci với chiến lược quy hoạch động mà thông qua một hàm khác, 
hàm này có chức năng tạo mảng gồm n + 1 phần tử, sau đó gọi hàm tính số Fibonacci thực sự với tham số là n và mảng vừa tạo.'''
# def nhap_so (n,a_lis):
#     if n < 3:
#         return 1
#     else:
#         a_lis = []
#         for i in range (3, len(a_lis)):
#             a_lis.append(i)
#             a_lis[i] = a_lis[len(a_lis)-1] + a_lis[len(a_lis)-2]
#         return a_lis[n]
# print(nhap_so(4,1))
# a_lis = [1,2.3,4,5,6]
# for i in range(3, len(a_lis)) :
#     a_lis[i] = a_lis[len(a_lis)- 1] + a_lis[len(a_lis) - 2]
# print(a_lis)



''''
Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
'''

# def ham_so_le (n):
#     count = 0
#     for i in n:
#        a = int(i)
#        if a %2 != 0  and a != 0:
#            count +=1
#     return count
#
# str = input('mời nhập chuỗi số: ')
# print(ham_so_le(str))
# DONE


'''
Viết hàm
        def change_upper_lower(str)
chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
mẫu
def change_upper_lower(str):
    res = []
    for c in str:
        if 'a' <= c <= 'z':
            res.append(chr(ord(c) - 32))
        elif 'A' <= c <= 'Z':
            res.append(chr(ord(c) + 32))
        else:
            res.append(c)
    return ''.join(res)
'''
# nhắc lại chr(): từ mã ascii về chữ
# còn ord(): từ chữ về mã ascii
# str = 'abcABCasdCVFadfe'

# def change_upper_lower(str):
#     res = []
#     for i in str :
#         if 'a' <= i <= 'z' :
#             res.append(chr(ord(i) - 32))
#         elif 'A' <= i <= 'Z' :
#             res.append(chr(ord(i) + 32))
#         else :
#             res.append(i)
#     return re_str.join(res)
# str = input('mời nhập: ')
# re_str = ''
# print(change_upper_lower(str))



'''
1. Viết hàm
        def body_mass_index(m, h)
để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
2. Viết hàm
        def bmi_information(m, h)
để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
công thức cân nặng / chiều cao* chiều cao
'''

def body_mass_index(m, h):
    bmi = round(float((m/(h**2))),2)
    return bmi
def bmi_information(m, h):
    bmi = float((m/(h**2)))
    if bmi < 18.5:
        print('Cân nặng thấp (gầy)')
    elif 18.5<bmi<24.9:
        print('bình thường')
    elif 25 < bmi < 29.9:
        print('thừa cân')
    elif 30 < bmi < 34.9:
        print('béo phì 1')
    elif 35 < bmi < 39.9:
        print('béo phì 2')
    elif bmi>40:
        print('béo phì 3')

m = int(input('nhập số cân: '))
h = float(input('nhập chiều cao: '))
print(f'chỉ số {body_mass_index(m,h)}')
print(bmi_information(m,h))



""" BÀI TẬP VỀ NHÀ BUỔI 07 - Function:

"""
'''
# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào


def max_min(*numbers):
    maxx = minn = numbers[0]
    for it in numbers:
        if it > maxx:
            maxx = it
        if it < minn:
            minn = it
    return maxx, minn


print(f'Max, min: {max_min(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 3, -3, -2)}')


# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str


def reverse_string(str):
    return str[::-1]


print(f'KQ: {reverse_string("chuoi can dao nguoc")}')


# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi


def is_perfect(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return True if tong_uoc == n else False


n = 8128
print(f'{n} là số hoàn hảo? {is_perfect(n)}')


# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = 5
print(f'{n} là số nguyên tố? {is_prime(n)}')


# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str


def count_upper_lower(str):
    hoa = thuong = 0
    for i in str:
        if 'A' <= i <= 'Z':
            hoa += 1
        elif 'a' <= i <= 'z':
            thuong += 1
    return hoa, thuong


print(f'chữ cái viết hoa, chữ cái viết thường: {count_upper_lower("string Demo count Hoa THUONG")}')


# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần


def is_pangram(str, alphabet):
    for c in alphabet:
        if c not in str:
            return False
    return True


str = '3010120130121'
alphabet = '0123'
print(f'{str} là Pangram? {is_pangram(str, alphabet)}')


# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j

import random


def create_matrix(n, m):
    return [[random.randrange(10) for j in range(m)] for i in range(n)]


n, m = 5, 4
res = create_matrix(n, m)
print(f'Matrix {n}x{m}:')
for i in range(n):
    print(res[i])


# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h


def body_mass_index(m, h):
    return m/h**2


def bmi_information(m, h):
    bmi = body_mass_index(m, h)
    print(f'Your BMI: {round(bmi, 1)}')
    if bmi < 15:
        print('=>> Very severely underweight')
    elif 15 <= bmi < 16:
        print('=>> Severely underweight')
    elif 16 <= bmi < 18.5:
        print('=>> Underweight')
    elif 18.5 <= bmi < 25:
        print('=>> Normal (healthy weight)')
    elif 25 <= bmi < 30:
        print('=>> Overweight')
    elif 30 <= bmi < 35:
        print('=>> Obese Class I (Moderately obese)')
    elif 35 <= bmi < 40:
        print('=>> Obese Class II (Severely obese)')
    else:
        print('=>> Obese Class III (Very severely obese)')


bmi_information(69, 1.73)


# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str


def change_upper_lower(str):
    res = []
    for c in str:
        if 'a' <= c <= 'z':
            res.append(chr(ord(c) - 32))
        elif 'A' <= c <= 'Z':
            res.append(chr(ord(c) + 32))
        else:
            res.append(c)
    return ''.join(res)


str = 'Demo thU xem SAO'
print(f'KQ: {change_upper_lower(str)}')


# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)


def count_odd(n):
    if n < 10:
        return n % 2
    else:
        return (n % 10) % 2 + count_odd(n//10)


n = 19922610
print(f'Số lượng số lẻ trong {n} là: {count_odd(n)}')

# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy


# Hàm đệ quy:
def tri_dequy(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tri_dequy(n-1) + tri_dequy(n-2) + tri_dequy(n-3)


n = 10
print(f'Tribonacci {n}: {tri_dequy(n)}')


# Hàm Không đệ quy
def tri_ko_dequy(n):
    f1, f2, f3 = 1, 1, 2
    f = 0
    if n <= 2:
        f = f2
    elif n == 3:
        f = f3
    else:
        for i in range(4, n+1):
            f = f3 + f2 + f1
            f3, f2, f1 = f, f3, f2
    return f


n = 3
print(f'Tribonacci {n}: {tri_ko_dequy(n)}')


# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1


def find_x(a_list, x):
    res = []
    for i in range(len(a_list)):
        if a_list[i] == x:
            res.append(i)
    return res


alist = [1, 2, 3, -4, 5, 6, 8, 9, 0, 3, 2, 1, 4, 5]
x = 3
print(f'Vị trí {x} trong list: {find_x(alist, x)}')


# Bài 13. Thực hiện code lại hàm sau và cho biết ý nghĩa của nó
#
# def enter_data():
#     while True:
#         n = input("Nhập 1 số nguyên: ")
#         if n.isnumeric():
#             n = int(n)
#             if n > 0:
#                 print("Đã nhập số dương")
#                 return n
#             print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
#         else:
#             print("Dữ liệu đã nhập không phải số nguyên")

print("Ý nghĩa: Giúp kiểm tra dữ liệu nhập vào phải là 1 số nguyên dương, nếu không thì sẽ yêu cầu nhập lại")
'''