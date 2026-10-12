import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертер JSON/CSV/XLSX")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("json2csv", "csv2json", "csv2xlsx"):
        command = commands.add_parser(name, help=name)
        command.add_argument("--in", dest="input", required=True, help="Входной файл")
        command.add_argument("--out", required=True, help="Выходной файл")
    args = parser.parse_args()
    if args.command == "json2csv":
        json_to_csv(args.input, args.out)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.out)
    else:
        csv_to_xlsx(args.input, args.out)
    print(f"Сохранено: {args.out}")


if __name__ == "__main__":
    main()
