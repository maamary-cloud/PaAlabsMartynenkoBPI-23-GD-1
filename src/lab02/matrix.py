def check_matrix(mat: list[list]) -> None:
    """Проверяет одинаковую длину строк."""
    if mat:
        for row in mat:
            if len(row) != len(mat[0]):
                raise ValueError("У матрицы строки разной длины")


def transpose(mat: list[list[float | int]]) -> list[list]:
    """Меняет строки и столбцы местами."""
    check_matrix(mat)
    result = []
    if not mat:
        return result
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        result.append(row)
    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает суммы строк прямоугольной матрицы."""
    check_matrix(mat)
    result = []
    for row in mat:
        result.append(sum(row))
    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает суммы столбцов прямоугольной матрицы."""
    return row_sums(transpose(mat))


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("transpose:", transpose(matrix))
    print("row_sums:", row_sums(matrix))
    print("col_sums:", col_sums(matrix))
