import json

from aeug.io.abc import AbstractWriter
from aeug.utils.typing import PathLike, Results


class JsonWriter(AbstractWriter):
    def __init__(self, path: PathLike, data: Results, index: int = 4) -> None:
        super().__init__(path, data, "json")
        self.index = index

    def write(self) -> None:
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.data, indent=self.index))
