def min_max(nums: list[float | int]) -> tuple:
    """Находит минимум и максимум циклом. Пустой список — ValueError."""
    if not nums:
        raise ValueError("Список пуст")
    smallest = largest = nums[0]
    for number in nums:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return smallest, largest


def unique_sorted(nums: list[float | int]) -> list:
    """Убирает повторы и сортирует пузырьком без sorted и sort."""
    result = []
    for number in nums:
        if number not in result:
            result.append(number)
    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def flatten(mat: list[list | tuple]) -> list:
    """Объединяет строки списков и кортежей; иначе TypeError."""
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Строка должна быть списком или кортежем")
        for item in row:
            result.append(item)
    return result


if __name__ == "__main__":
    print("min_max:", min_max([3, -1, 5, 5, 0]))
    print("unique_sorted:", unique_sorted([3, 1, 2, 1, 3]))
    print("flatten:", flatten([[1, 2], (3, 4)]))
