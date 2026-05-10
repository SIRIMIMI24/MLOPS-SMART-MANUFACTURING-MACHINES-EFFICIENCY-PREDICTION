"""Phase 1 scaffold checks for future model implementation."""

from pathlib import Path


def test_models_directory_exists():
    assert Path("models").is_dir()
