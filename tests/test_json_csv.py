import csv
import json
import pytest
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv(tmp_path):
    source = tmp_path / "people.json"
    result = tmp_path / "people.csv"
    source.write_text(
        '[{"name": "Алиса", "age": 22}, {"name": "Боб", "age": 25}]', encoding="utf-8"
    )
    json_to_csv(source, result)
    with result.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames == ["name", "age"]
        rows = list(reader)
    assert rows == [{"name": "Алиса", "age": "22"}, {"name": "Боб", "age": "25"}]


def test_csv_to_json(tmp_path):
    source = tmp_path / "people.csv"
    result = tmp_path / "people.json"
    source.write_text("name,age\nАлиса,22\nБоб,25\n", encoding="utf-8")
    csv_to_json(source, result)
    data = json.loads(result.read_text(encoding="utf-8"))
    assert data == [{"name": "Алиса", "age": "22"}, {"name": "Боб", "age": "25"}]


def test_missing_fields(tmp_path):
    source = tmp_path / "people.json"
    result = tmp_path / "people.csv"
    source.write_text('[{"name": "Алиса"}, {"age": 25}]', encoding="utf-8")
    json_to_csv(source, result)
    with result.open(encoding="utf-8", newline="") as file:
        assert list(csv.DictReader(file)) == [
            {"name": "Алиса", "age": ""},
            {"name": "", "age": "25"},
        ]


@pytest.mark.parametrize("content", ["", "{", "[]", "{}", '["text"]'])
def test_bad_json(tmp_path, content):
    source = tmp_path / "bad.json"
    source.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(source, tmp_path / "result.csv")


@pytest.mark.parametrize(
    "content", ["", "\n", "name,name\nA,B", "name,age\nA,22,extra", ",age\nA,22"]
)
def test_bad_csv(tmp_path, content):
    source = tmp_path / "bad.csv"
    source.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(source, tmp_path / "result.json")


def test_missing_files(tmp_path):
    with pytest.raises(FileNotFoundError):
        json_to_csv(tmp_path / "missing.json", tmp_path / "result.csv")
    with pytest.raises(FileNotFoundError):
        csv_to_json(tmp_path / "missing.csv", tmp_path / "result.json")
