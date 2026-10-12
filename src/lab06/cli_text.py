import argparse
from src.lab04.io_txt_csv import read_text
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="Вывод текста и статистика")
    commands = parser.add_subparsers(dest="command", required=True)
    cat = commands.add_parser("cat", help="Вывести файл")
    cat.add_argument("--input", required=True, help="Путь к файлу UTF-8")
    cat.add_argument("-n", action="store_true", help="Номера строк")
    stats = commands.add_parser("stats", help="Частоты слов")
    stats.add_argument("--input", required=True, help="Путь к файлу UTF-8")
    stats.add_argument("--top", type=int, default=5, help="Количество слов")
    args = parser.parse_args()
    if args.command == "stats" and args.top < 0:
        parser.error("--top должен быть неотрицательным")
    text = read_text(args.input)
    if args.command == "cat":
        for number, line in enumerate(text.splitlines(), 1):
            if args.n:
                print(f"{number}: {line}")
            else:
                print(line)
    else:
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print(f"Топ-{args.top}:")
        for word, count in top_n(freq, args.top):
            print(f"{word}:{count}")


if __name__ == "__main__":
    main()
