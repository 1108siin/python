while True :
    money = int(input("투입한 돈: "))
    name = input("물건명: ")
    price = int(input(f"{name}물건값: "))
    if(money<price):
        print("금액이 부족합니다")
    else:
        change = money - price
        print("거스름돈: ", change)
        coin500s = change // 500
        change = change % 500
        coin100s = change // 100

        print("500원 동전 개수: ", coin500s)
        print("100원 동전 개수: ", coin100s)
    end = input("계속하시겠습니까? (y/n) ")
    if(end== "N" or end== "n"):
        break
print("\n종료합니다")