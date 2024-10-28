from abc import ABC, abstractmethod
from pathlib import Path
from typing import Literal

from aeug.utils.typing import PathLike, Results


class AbstractWriter(ABC):
    def __init__(
        self, path: PathLike, data: Results, supported_extension: str
    ) -> None:
        self.path = Path(path) if isinstance(path, str) else path
        self.data = data
        self.supported_extension = supported_extension

    @abstractmethod
    def write(self) -> None:
        raise NotImplementedError

    def check_extension(self) -> Literal[True]:
        ext = self.path.suffix
        if ext.startswith("."):
            ext = ext[1:]
        if ext != self.supported_extension:
            raise ValueError(f"Invalid extension: {ext}")

        return True
