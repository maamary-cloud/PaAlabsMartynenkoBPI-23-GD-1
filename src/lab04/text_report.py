import argparse
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="Частоты слов в одном файле")
    parser.add_argument("--in", dest="input", default="data/lab04/input.txt")
    parser.add_argument("--out", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()
    tokens = tokenize(normalize(read_text(args.input, args.encoding)))
    freq = count_freq(tokens)
    write_csv(top_n(freq, len(freq)), args.out, ("word", "count"))
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
