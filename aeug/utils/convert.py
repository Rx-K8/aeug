import json
from abc import ABC, abstractmethod

from aeug.utils.typing import CommonSearchOutput, ValidationFormat


class BaseConvert(ABC):
    @abstractmethod
    def to_common_search_output(
        self, query: str, doc: str, rank: int, score: float
    ) -> CommonSearchOutput:
        raise NotImplementedError

    def to_val_format(self, topic_id, search_output: CommonSearchOutput):
        return ValidationFormat(
            topic_id=topic_id,
            doc_id=search_output.doc_id,
            rank=search_output.rank,
            score=search_output.score,
        )


class BEIRConvert(BaseConvert):
    def to_common_search_output(
        self, query: str, doc: str, rank: int, score: float
    ):
        dict_doc = json.loads(doc)
        return CommonSearchOutput(
            query=query,
            content=dict_doc["text"],
            doc_id=dict_doc["_id"],
            rank=rank,
            score=score,
        )


class TRECConvert(BaseConvert):
    def to_common_search_output(
        self, query: str, doc: str, rank: int, score: float
    ):
        dict_doc = json.loads(doc)
        return CommonSearchOutput(
            query=query,
            content=dict_doc["contents"],
            doc_id=dict_doc["id"],
            rank=rank,
            score=score,
        )


CONVERTERS = {"beir_trec_covid": BEIRConvert(), "trec2020": TRECConvert()}
