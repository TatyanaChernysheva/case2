from random import randint

x = randint(1, 10)
print(x)
num = 0
attemp = 0
tries = 0

while True:
    print("Привет, я загадал число от 1 до 10, угадай его")
    num = int(input("Твоя догадка:"))
    attemp += 1
    tries += 1
    if num == x:
        print("А ты хорош, угадал число!\nКоличество твоих попыток: " + str(attemp) + "Спасибо за игру")
        break
    if num > x:
        print("НЕ верно, меньше")
    if num < x:
        print("Число больше")
    if num != x and tries == 6:
        print(f"Прости попыкти кончились, попробуй снова. Мое число было: {x} ")