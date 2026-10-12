import pytest
from src.lab04.io_txt_csv import read_text, write_csv


def test_read_and_write(tmp_path):
    source = tmp_path / "input.txt"
    source.write_text("Привет", encoding="utf-8")
    assert read_text(source) == "Привет"
    result = tmp_path / "report.csv"
    write_csv([("привет", 1)], result, ("word", "count"))
    assert result.read_text(encoding="utf-8").splitlines() == ["word,count", "привет,1"]


def test_empty(tmp_path):
    source = tmp_path / "empty.txt"
    source.write_text("", encoding="utf-8")
    assert read_text(source) == ""
    result = tmp_path / "empty.csv"
    write_csv([], result, ("word", "count"))
    assert result.read_text(encoding="utf-8").strip() == "word,count"
    write_csv([], result)
    assert result.read_text(encoding="utf-8") == ""


def test_cp1251(tmp_path):
    source = tmp_path / "input.txt"
    source.write_text("Привет", encoding="cp1251")
    assert read_text(source, "cp1251") == "Привет"


def test_different_lengths(tmp_path):
    with pytest.raises(ValueError):
        write_csv([("a", 1), ("b",)], tmp_path / "bad.csv")
