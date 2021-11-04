user_input_a = input("정수입력 >")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름: ", number_input_a)
else:
    print("정수가 아닙니다.")

# try -except

try:
    user_input_a = input("정수입력 >")
    number_input_a = int(user_input_a)
except:
    print("예외발생")

else:
    print("원의 반지름: ", number_input_a)
finally:
    print("예외구문 끝")

# 예외처리고급

list_number = [52, 273, 32, 72, 100]

try:
    number_input_a = int(input(user_input_a))
    print("{}번째 요소 ; {}".format(number_input_a, list_number[number_input_a]))
    예외.발생
except ValueError as exception:
    print(type(exception), exception)

except IndexError as exception:
    print(type(exception), exception)
except Exception as exception:
    print(type(exception), exception)


# 데코레이터

def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")

    return wrapper


@test
def hello():
    print("hello")


hello()
