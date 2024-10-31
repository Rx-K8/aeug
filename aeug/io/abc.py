from abc import ABC, abstractmethod
from pathlib import Path
from typing import Literal

from aeug.utils.typing import PathLike, WriteOutput


class AbstractWriter(ABC):
    def __init__(self, file_path: PathLike, supported_extension: str) -> None:
        self.file_path: Path = (
            Path(file_path) if isinstance(file_path, str) else file_path
        )
        self.supported_extension = supported_extension

        if not self.check_extension():
            raise ValueError(f"Invalid extension: {self.file_path.suffix}")

    @abstractmethod
    def write(self, data: list[str]) -> None:
        raise NotImplementedError

    def check_extension(self) -> Literal[True]:
        ext = self.file_path.suffix
        if ext.startswith("."):
            ext = ext[1:]
        if ext != self.supported_extension:
            raise ValueError(f"Invalid extension: {ext}")

        return True

    def make_dir(self) -> None:
        dir_path: Path = self.file_path.parent
        dir_path.mkdir(exist_ok=True, parents=True)
