from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    text = input()
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
