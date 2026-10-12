import pytest
from src.lab02.arrays import min_max, unique_sorted, flatten
from src.lab02.matrix import transpose, row_sums, col_sums
from src.lab02.tuples import format_record


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, -1, 5, 5, 0], (-1, 5)),
        ([42], (42, 42)),
        ([-5, -2, -9], (-9, -2)),
        ([1.5, 2, 2.0, -3.1], (-3.1, 2)),
    ],
)
def test_min_max(nums, expected):
    assert min_max(nums) == expected


def test_min_max_empty():
    with pytest.raises(ValueError):
        min_max([])


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 2, 1, 3], [1, 2, 3]),
        ([], []),
        ([-1, -1, 0, 2, 2], [-1, 0, 2]),
        ([1.0, 1, 2.5, 2.5, 0], [0, 1.0, 2.5]),
    ],
)
def test_unique_sorted(nums, expected):
    assert unique_sorted(nums) == expected


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([[1, 2], (3, 4, 5)], [1, 2, 3, 4, 5]),
        ([[1], [], [2, 3]], [1, 2, 3]),
    ],
)
def test_flatten(mat, expected):
    assert flatten(mat) == expected


def test_flatten_bad_row():
    with pytest.raises(TypeError):
        flatten([[1, 2], "ab"])


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
        ([], []),
    ],
)
def test_transpose(mat, expected):
    assert transpose(mat) == expected


@pytest.mark.parametrize(
    "mat, rows, cols",
    [
        ([[1, 2, 3], [4, 5, 6]], [6, 15], [5, 7, 9]),
        ([[-1, 1], [10, -10]], [0, 0], [9, -9]),
        ([[0, 0], [0, 0]], [0, 0], [0, 0]),
    ],
)
def test_sums(mat, rows, cols):
    assert row_sums(mat) == rows
    assert col_sums(mat) == cols


@pytest.mark.parametrize("function", [transpose, row_sums, col_sums])
def test_ragged(function):
    with pytest.raises(ValueError):
        function([[1, 2], [3]])


@pytest.mark.parametrize(
    "record, expected",
    [
        (
            ("Иванов Иван Иванович", "BIVT-25", 4.6),
            "Иванов И.И., гр. BIVT-25, GPA 4.60",
        ),
        (("Петров Пётр", "IKBO-12", 5.0), "Петров П., гр. IKBO-12, GPA 5.00"),
        (
            ("Петров Пётр Петрович", "IKBO-12", 5.0),
            "Петров П.П., гр. IKBO-12, GPA 5.00",
        ),
        (
            ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
            "Сидорова А.С., гр. ABB-01, GPA 4.00",
        ),
    ],
)
def test_record(record, expected):
    assert format_record(record) == expected


@pytest.mark.parametrize(
    "record",
    [
        ("", "A", 4),
        ("Иванов Иван", "", 4),
        ("Иванов Иван", "A", "4"),
        ("Иванов Иван", "A", 6),
    ],
)
def test_bad_record(record):
    with pytest.raises((ValueError, TypeError)):
        format_record(record)
