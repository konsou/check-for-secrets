from pathlib import Path
from typing import Generator, NamedTuple


class FileNameAndContent(NamedTuple):
    name: str
    content: str


def file_contents(directory: str) -> Generator[FileNameAndContent, None, None]:
    """
    Yields the contents of all files in the given directory.
    """
    path = Path(directory)
    for file in path.iterdir():
        if file.is_file():
            with file.open("r", encoding="utf-8") as f:
                yield FileNameAndContent(file.name, f.read())
