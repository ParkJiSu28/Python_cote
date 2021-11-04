print("보이류\n 하이  \t 안농")

print('''\
안
녕
하
세
요\
''')

print("안녕하세요"[0:2])

print("안녕하세요"[3:])

print(3 // 2)
print(3 ** 2)

format_a = "{}만원".format(5000)
print(format_a)

output = "{:05d}".format(52)

print(output)

output_a = 52.0
print("{:g}".format(output_a))

a = "qkrwltn"

print(a.upper())
print(a.lower())

b = "asdasdasd"

print(b.find("s"))

a = "10 20 30 40 50 60 80 90 100".split(" ")
print(a)

print(a[2])

b = int(a[2])
print(10 < b < 30)

if b > 0:
    print(b)

import datetime

now = datetime.datetime.now()

print(now.year)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

# number = input("정수입력>")

last_c = 8

if last_c % 2 == 0:
    print("짝수")
elif last_c == 9:
    print("9이네")
else:
    print("홀수")

list_a = [273, "asdasdas", 12345]

print(list_a[0])

print(list_a[1])

print(list_a[1][3])

l = [[273, 456], ["asdasd"]]

print(l[0][1])

# list 값 추가 메소드
list_a.append(8)
list_a.insert(0, 9)
print(list_a)
list_a.extend([1, 2, 30])
print(list_a)

# 삭제

del list_a[0]

print(list_a)

list_a.pop(0)

print(list_a)

list_a.remove(8)

print(list_a)

list_a.clear()
print(list_a)

# list값 확인
list_a = [273, "asdasdas", 12345]

if 273 in list_a:
    print(273 in list_a)

if 99 in list_a:
    pass
else:
    print(99 not in list_a)

# for 문

for i in range(10):
    print(i)

for asd in list_a:
    print(asd)

for cha in "개새끼야":
    print(cha)

# 딕셔너리

dict_a = {
    "name": "어벤져스 엔드게임",
    "type": "히어로무비",
    "char": ["아이언맨", "헐크", "블랙위도우"]
}

print(dict_a)
print(dict_a["name"])
print(dict_a["type"])
print(dict_a["char"][0])

# 딕셔너리 삭제

del dict_a["type"]
print(dict_a)

# 딕셔너리 내부에 키가 있는지 확인

print("char" in dict_a)

value = dict_a.get("char1")
print(value)
# 딕셔너리 반복문

for key in dict_a:
    print(key, ":", dict_a[key])

# 범위 반복문
# range(A) 0~A-1  range(A,B) A~B-1 range(A,B,C) A~B-1 C만큼 차이
print(list(range(10)))
print(list(range(10, 20)))
print(list(range(10, 20, 2)))

print(list(range(0, 10 // 2)))  # 무조건 정수여야하기때문에

# 역반복문

for i in range(4, -1, -1):
    print("현재 반복변수 :{}".format(i))
for i in reversed(range(5)):
    print("현재 반복변수 :{}".format(i))

# while문 리스트

value = 2
l = [1, 2, 1, 2]

while value in l:
    l.remove(value)

print(l)

# list 기본 함수

num = [103, 52, 279, 32, 77]
print(min(num))
print(max(num))
print(sum(num))

num_reverse = reversed(num)

print(num_reverse)

for i in num_reverse:
    print("첫번째{}".format(i))

for i in num_reverse:
    print("두번째{}".format(i))

# enumerate()

exam = ["A", "B", "C"]

print(enumerate(exam))

print(list(enumerate(exam)))

for i, value in enumerate(exam):
    print("{}번째 요소는 {}입니다.".format(i, value))  # enumerate 함수를 사용해야 for문을 저렇게 사용할 수 있다.

# 딕셔너리의 items()함수와 반복문 조합

exam_d = {
    "A": "1",
    "B": "2",
    "C": "3"
}

print(exam_d.items())

for key, element in exam_d.items():
    print("dict[{}] = {}".format(key, element))

# 반복을 사용하여 리스트 만들기  리스트 컴프리헨션 중요하다

array = []

for i in range(0, 20, 2):
    array.append(i * i)
print(array)

# 같은 내용을 한줄로

array = [i * i for i in range(0, 20, 2)]
print(array)

array = [i * i for i in range(0, 20, 2) if i * i == 64]
print(array)


# 긴 구문은 ()안에 적자 ex) print(("asdasdasdadas\n" asdasdasdasd))
# 아니면 join() 사용


# 함수

def print_n_time(n, *values):
    for i in range(n):
        for value in values:
            print(value)
    print()


print_n_time(5, "a", "12312", 123456)


def sum_all(start, end, step):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output


print(sum_all(0, 100, 2))


# 팩토리얼 반복문 or 재귀호출

def fact(i):
    output = 1
    for a in range(1, i + 1):
        output *= a
    return output


print(fact(3))


# 재귀 fact(n) = n* fact(n-1)

def fact1(n):
    if n == 0:
        return 1

    else:
        return n * fact(n - 1)


print(fact1(3))


# 피보나치 fibo(n) = fibo(n-1) +fibo(n-2)

def fibo(n):
    if n == 1:
        return 1

    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(5))

# 향상된 피보나치수열 메모화

dict_a = {
    1: 1,
    2: 1
}


def fibo1(n):
    if n in dict_a:
        return dict_a[n]
    else:
        output = fibo1(n - 1) + fibo1(n - 2)
        dict_a[n] = output
        return output


print(fibo1(50))

# 괄호가 없는 튜플

tuple_test = 10, 20, 30, 40
print(tuple_test)

a, b, c = 10, 20, 30

print(a)
print(b)

# 값을 교환하는 튜플

a, b = 10, 20

print(a, b)

a, b = b, a
print(a, b)


# 여러개의 값을 교환하기

def test():
    return (10, 20)


a, b = test()

print(a, b)


# 함수의 매개변수로 함수 전달하기

def call_10_times(func):
    for i in range(10):
        func()


def print_hello():
    print("hello")


call_10_times(print_hello)


# map과 filter

def power(item):
    return item * item


list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)

print("# map의 실행결과")
print(output_a)
print(list(output_a))


def under_3(item):
    return item < 3


output_b = filter(under_3, list_input_a)
print("# filter의 실행결과")
print(output_b)
print(list(output_b))

#람다로 바꾸기

power1 = lambda x: x*x
upder_31 = lambda  x: x<3

output_a = map(power1,list_input_a)
print(list(output_a))

output_b = filter(upder_31, list_input_a)
print(list(output_b)


# 예외처리


