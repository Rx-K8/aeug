import json

from aeug.io.abc import AbstractWriter
from aeug.utils.typing import PathLike


class JsonWriter(AbstractWriter):
    def __init__(self, path: PathLike, index: int = 4) -> None:
        super().__init__(path, "json")
        self.index = index

    def write(self, data: list[str]) -> None:
        self.make_dir()
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=self.index))
