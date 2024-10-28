import os
from typing import TypedDict, Union

PathLike = Union[str, os.PathLike]


class ResultDict(TypedDict):
    query_id: str
    query: str
    rank: int
    score: float


Results = list[ResultDict]
