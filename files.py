from pathlib import Path
from typing import Generator, NamedTuple

import tiktoken


class FileNameAndContent(NamedTuple):
    name: str
    content: str
    content_in_chunks: list[str]


def file_contents(directory: str) -> Generator[FileNameAndContent, None, None]:
    """
    Yields the contents of all files in the given directory.
    """
    path = Path(directory)
    for file in path.iterdir():
        if file.is_file():
            with file.open(
                "r",
                encoding="utf-8",
                errors="replace",
            ) as f:
                file_content = f.read()
                yield FileNameAndContent(
                    file.name, file_content, split_into_chunks(file_content)
                )


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    """Counts the number of tokens in a given string."""
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def split_into_chunks(
    text: str, max_tokens: int = 1500, encoding_name: str = "cl100k_base"
) -> list[str]:
    """Splits a long text into chunks that fit within the token limit."""
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)

    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunks.append(encoding.decode(chunk_tokens))

    return chunks
