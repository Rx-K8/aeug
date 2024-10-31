from aeug.io.abc import AbstractWriter
from aeug.utils.typing import PathLike


class JsonlWriter(AbstractWriter):
    def __init__(self, path: PathLike, index: int = 4) -> None:
        super().__init__(path, "jsonl")
        self.index = index

    def write(self, data: list[str]) -> None:
        self.make_dir()
        with open(self.file_path, "w", encoding="utf-8") as file:
            for entry in data:
                file.write(entry + "\n")
