import tkinter as tk


def print_matrix(matrix):
    """Подстройка под максимальную длину и вывод матрицы"""
    if matrix:
        print('-' * 75)
        print("Matrix:")
        max_length = max(len(str(item)) for row in matrix for item in row)
        for row in matrix:
            formatted_row = " | ".join(f"{str(item).rjust(max_length)}" for item in row)
            print(f"| {formatted_row} |")
        print('-' * 75)


def get_index_row_col(n):
    if n % 2 == 0:
        curr_row, curr_col = n // 2, n // 2 - 1
    else:
        curr_row, curr_col = n // 2, n // 2
    return curr_row, curr_col


def bypass_matrix(n):
    num = 1  # текущее число для заполнения матрицы
    step_move = 1  # сколько двигаться в разную сторону
    need_num = n ** 2  # число окончания
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    curr_row, curr_col = get_index_row_col(n)

    matrix[curr_row][curr_col] = num

    while True:
        # вправо
        for i in range(step_move):
            if num >= need_num:
                return matrix
            num += 1
            curr_col += 1
            matrix[curr_row][curr_col] = num

        # вверх
        for i in range(step_move):
            num += 1
            curr_row -= 1
            matrix[curr_row][curr_col] = num

        step_move += 1
        # влево
        for i in range(step_move):
            if num >= need_num:
                return matrix
            num += 1
            curr_col -= 1
            matrix[curr_row][curr_col] = num

        # вниз
        for i in range(step_move):
            num += 1
            curr_row += 1
            matrix[curr_row][curr_col] = num
        step_move += 1


def check_simple_num(num):
    if num < 2:
        return False
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def draw(n, matrix):
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.title("Ковёр Улама")

    canvas = tk.Canvas(root, width=width, height=height, bg="white")

    k = min(width, height) // (n * 1.25)  # шаг сетки
    half = k // 2  # половина стороны квадрата в пикселях
    center = (n - 1) / 2

    for i in range(n):
        for j in range(n):
            x = int(width / 2 + (j - center) * k)
            y = int(height / 2 + (i - center) * k)

            if check_simple_num(matrix[i][j]):
                canvas.create_rectangle(
                    x - half, y - half,
                    x + half, y + half,
                    fill="black", outline=""
                )

    canvas.pack()
    root.mainloop()


def main():
    n = 322
    matrix = bypass_matrix(n)
    # print_matrix(matrix)
    draw(n, matrix)


if __name__ == "__main__":
    main()
