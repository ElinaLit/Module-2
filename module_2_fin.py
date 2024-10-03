a = int(input('Введите номер от 3 до 20: '))
result = []
for b in range(1, a):
    for c in range(1, a):
            if a % (b + c) == 0 or (b+c) % a ==0:
                result.append([b, c])
print(result)
