# #match.py
# #조건문 match_case
# num = int(input("1~3숫자입력 > "))
# match num:
#     case 1:
#         print("1 입력")
#     case 2:
#         print("2 입력")
#     case 3:
#         print("3 입력")
#     case _:
#         print('1~3 이외의 숫자')

num1 = int(input("짝수입력 > "))
num2 = int(input("홀수입력 > "))
match num1 % 2, num2 % 2:
    case 0, 1:
        print("num1은 짝수 num2는 홀수")
    case 0, _:
        print("num1은 짝수")
        #num1은 짝수(0), num2는 어떤 숫자든 상관없는 경우
    case _, 1:
        print("num2는 홀수")
    case _:
        print("둘 다 오류")
        #위의 모든 경우에 해당하지 않는 경우
    
#하나의 수를 입력받고,
#그 수가 3, 5의 배수인지 확인하여
# '3과 5의 배수', '3의배수' '5의배수' '둘다아님'을 출력하시오