import json

from aeug.io.abc import AbstractWriter
from aeug.utils.typing import PathLike, Results


class JsonlWriter(AbstractWriter):
    def __init__(self, path: PathLike, data: Results, index: int = 4) -> None:
        super().__init__(path, data, "jsonl")
        self.index = index

    def write(self) -> None:
        with open(self.path, "w", encoding="utf-8") as file:
            for entry in self.data:
                file.write(entry + "\n")
