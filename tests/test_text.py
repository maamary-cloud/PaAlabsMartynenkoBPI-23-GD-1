import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


def test_normalize_options():
    assert normalize("ЁЖИК", yo2e=False) == "ёжик"
    assert normalize("Straße", casefold=False) == "straße"
    assert normalize("Straße") == "strasse"


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize(source, expected):
    assert tokenize(source) == expected


def test_count_freq():
    assert count_freq(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert count_freq([]) == {}


def test_top_n():
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(freq, 0) == []
    assert top_n({}, 5) == []


def test_top_n_tie():
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 2) == [("aa", 2), ("bb", 2)]
