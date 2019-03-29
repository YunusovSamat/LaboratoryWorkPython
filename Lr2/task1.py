def group(values, n):
    h = int(len(values) / n)
    mas = [0] * h

    for i in range(h):
        mas[i] = [0] * n
        for j in range(n):
            mas[i][j] = values[i * n + j]

    return mas


def read_sudoku(file):
    digits = [c for c in open(file).read() if c in '123456789.']
    values = group(digits, 9)
    return values


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def get_block(values, pos):
    row, col = pos
    row = row // 3
    col = col // 3
    arr = []

    for i in range(3):
        for j in range(3):
            arr.append(values[row * 3 + i][col * 3 + j])

    return arr


def get_row(values, pos):
    row, col = pos
    arr = values[row]

    return arr


def get_col(values, pos):
    row, col = pos
    arr = []

    for i in range(9):
        arr.append(values[i][col])

    return arr


def find_empty_positions(values):
    for i in range(len(values)):
        if "." in values[i]:
            return i, values[i].index(".")

    return -1, -1


def find_possible_values(values, pos):
    row, col = pos
    s = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    return s - set(get_block(values, pos)) - set(get_row(values, pos)) - set(get_col(values, pos))


def check_solution(values):
    s = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    for i in range(9):
        if s != set(get_row(values, (i,0))):
            return False
        if s != set(get_col(values, (0, i))):
            return False
        if s != set(get_block(values, (i // 3, i % 3))):
            return False

    return True


def solve(values):
    pos = find_empty_positions(values)

    for i in find_possible_values(values, pos):
        if check_solution(values):
            return values

        values[pos[0]][pos[1]] = i
        solve(values)

    if check_solution(values):
        return values

    values[pos[0]][pos[1]] = "."


file_name = "S:\Home\коды_Python3\Задания_с_сайта\лр№2\судоку.txt"
array = read_sudoku(file_name)
display(array)

print()
display(solve(array))


