import re
import unicodedata


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Приводит регистр, заменяет ё и схлопывает пробелы."""
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    result = ""
    for symbol in text:
        if unicodedata.category(symbol).startswith("C"):
            result += " "
        else:
            result += symbol
    return " ".join(result.split())


def tokenize(text: str) -> list[str]:
    """Выделяет слова, включая числа и внутренние дефисы."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает слова обычным словарём."""
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Сортирует по частоте вниз, затем по алфавиту."""
    if n < 0:
        raise ValueError("N не может быть отрицательным")
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
