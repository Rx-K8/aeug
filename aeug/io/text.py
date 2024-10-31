from aeug.io.abc import AbstractWriter
from aeug.utils.typing import PathLike, WriteOutput


class TextWriter(AbstractWriter):
    def __init__(self, path: PathLike) -> None:
        super().__init__(path, "txt")

    def write(self, data: list[str]) -> None:
        self.make_dir()
        with open(self.file_path, "w") as f:
            f.write("\n".join(data))
