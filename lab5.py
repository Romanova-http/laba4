import random

def kamni(n):
    while n > 0:
        print("Осталось камней:", n)
        try:
            vibor1 = int(input("Ваш ход. Введите количество камней (1, 2 или 3): "))
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 3.")
            continue
        
        if vibor1 < 1 or vibor1 > 3:
            print("Некорректный ввод. Введите число от 1 до 3.")
            continue
        if vibor1 >= n:
            print("Компьютер победил!")
            break
        n -= vibor1
        vibor2 = random.randint(1, 3)
        print("Ход компьютера. Компьютер взял", vibor2, "камней.")
        if vibor2 >= n:
            print("Вы победили!")
            break
        n -= vibor2

n = random.randint(4, 30)
print("Игра началась! Всего камней:", n)
kamni(n)
