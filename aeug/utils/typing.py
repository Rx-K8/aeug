import os
from typing import Union

from pydantic import BaseModel

PathLike = Union[str, os.PathLike]


class CommonSearchOutput(BaseModel):
    query: str
    doc_id: str
    content: str
    rank: int
    score: float


class ValidationFormat(BaseModel):
    """Validation format for TREC.

    For more details, please refer to the following link:
    https://ir.nist.gov/covidSubmit/round1.html

    Args:
        topic_id: The topic number.
        q0: The literal 'Q0'. (unused)
        doc_id: The identifier of the retrieved document.
        rank: The rank position of this document in the list.
        score: The similarity score computed by the system for this document.
        run_tag: A name assigned to the run. (unused)
    """

    topic_id: Union[int, str]
    q0: str = "Q0"
    doc_id: str
    rank: int
    score: float
    run_tag: str = "anserini"
