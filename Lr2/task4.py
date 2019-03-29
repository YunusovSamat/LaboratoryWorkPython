import random


def create_base(mas):
    arr = list("123456789")
    k = 0

    for i in range(3):
        for j in range(3):
            mas[i*3 + j] = arr[k:] + arr[: k]
            k += 3
        k -= 8
    return mas


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def transposing_arr(mas):
    global array
    array = list(map(list, zip(*mas)))
    return array


def swap_rows(mas, a, b):
    arr = mas[a]
    mas[a] = mas[(a//3) * 3 + b]
    mas[(a // 3) * 3 + b] = arr
    return mas


def swap_columns(mas, a, b):
    mas = transposing_arr(mas)
    swap_rows(mas, a, b)
    mas = transposing_arr(mas)
    return mas


def swap_rows_part(mas, a, b):
    for i in range(3):
        arr = mas[a*3 + i]
        mas[a*3 + i] = mas[b*3 + i]
        mas[b*3 + i] = arr
    return mas


def swap_columns_part(mas, a, b):
    mas = transposing_arr(mas)
    swap_rows_part(mas, a, b)
    mas = transposing_arr(mas)
    return mas


def mix_arr(mas):
    if random.randint(0, 1):
        transposing_arr(array)

    for i in range(random.randint(10, 20)):
        x = random.randint(0, 8)
        y = random.randint(0, 2)
        mas = swap_rows(mas, x, y)

    for i in range(random.randint(10, 50)):
        x = random.randint(0, 8)
        y = random.randint(0, 2)
        mas = swap_columns(mas, x, y)

    for i in range(random.randint(10, 50)):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        mas = swap_rows_part(mas, x, y)

    for i in range(random.randint(10, 20)):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        mas = swap_columns_part(mas, x, y)

    return mas


def del_cell(mas, e):
    arr = [[0 for i in range(9)] for j in range(9)]
    n = 0
    while n < (81-e):
        a = random.randint(0, 8)
        b = random.randint(0, 8)

        if arr[a][b] == 0:
            arr[a][b] = 1
            n += 1
            mas[a][b] = "."

    return mas


array = [""] * 9
for L in range(9):
    array[L] = [""] * 9

display(create_base(array))
display(mix_arr(array))

while True:
    d = int(input("Введите число заполненых элементов: "))
    if (d > 20) and (d <= 81):
        break

display(del_cell(array, d))

