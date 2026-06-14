# src/png_validation.py

from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def file_exists(file_path: str) -> bool:
    """
    Check whether the file exists.
    """
    return Path(file_path).is_file()


def has_png_extension(file_path: str) -> bool:
    """
    Check whether the file has a .png extension.
    """
    return Path(file_path).suffix.lower() == ".png"


def is_not_empty(file_path: str) -> bool:
    """
    Check whether the file is not empty.
    """
    return Path(file_path).stat().st_size > 0


def verify_png_signature(file_path: str) -> bool:
    """
    Verify the PNG magic bytes.
    """
    with open(file_path, "rb") as file:
        signature = file.read(8)

    return signature == PNG_SIGNATURE


def validate_png_file(file_path: str) -> None:
    """
    Run all PNG validation checks.
    Raises an exception if validation fails.
    """

    if not file_exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not has_png_extension(file_path):
        raise ValueError("Invalid file extension. Expected .png")

    if not is_not_empty(file_path):
        raise ValueError("File is empty.")

    if not verify_png_signature(file_path):
        raise ValueError("Invalid PNG signature.")
