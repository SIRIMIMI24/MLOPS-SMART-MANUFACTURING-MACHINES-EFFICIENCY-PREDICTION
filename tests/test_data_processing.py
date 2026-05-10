"""Phase 1 scaffold checks for future data processing implementation."""

from pathlib import Path


def test_data_directories_exist():
    assert Path("data/raw").is_dir()
    assert Path("data/processed").is_dir()
