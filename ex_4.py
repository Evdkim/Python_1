a = int(input("Введите целое положительное число - "))
b = 0
c = a
while c > 0:
    d = c % 10
    if d > b:
        b = d
        if b == 9:
         break
    c = c // 10
print(f"максимальная цифра в {a} = {b}")

