N = int(input('Введите количество монет '))
o = r = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        o += 1
    else:
        r += 1
if o < r:
    print(f'Переверните {o} монет с орла на решку, их минимальное количество')
elif o == r:
    print(f'Количество орлов и решек одинаково, по {o} штук')
else:
    print((f'Переверните {r} монет с решки на орла, их минимальное количество'))



a = int(input('Введите сумму двух чисел '))
b = int(input('Введите произведение чисел '))
c = 0
for i in range(a + b):
    if c:
        break
    for j in range(a + b):
        if i + j == a and i * j == b:
            c = 1
            print((f'первое загаданное число ="{i}", второе загаданное число ="{j}"'))
            break




N = abs(int(input('Введите число N ')))
stop = 0
P = 2
for i in range(N):
    if stop != 1:
        P = P ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = N
