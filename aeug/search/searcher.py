import json
from abc import ABC, abstractmethod

from pyserini.search import FaissSearcher, LuceneSearcher
from pyserini.search.faiss import AutoQueryEncoder


class VectorSearcher(SearcherBase):
    def __init__(
        self, query_encoder_id: str, document_id: str = "msmarco-v1-passage"
    ):
        self.query_encoder = AutoQueryEncoder(
            encoder_dir=query_encoder_id, pooling="mean"
        )
        self.searcher = FaissSearcher(
            "contriever_msmarco_index/", self.query_encoder
        )
        self.corpus = LuceneSearcher.from_prebuilt_index(document_id)

    def search(self, hyde_vector):
        hits = self.searcher.search(hyde_vector, 10)
        return hits

    def get_document(self, hit):
        return self.corpus.doc(hit.docid).raw()

    def get_documents(self, hyde_vector):
        hits = self.search(hyde_vector)
        results = []
        for i, hit in enumerate(hits, 1):
            result = {
                "query_id": hit.docid,
                "rank": i,
                "score": hit.score,
            }
            results.append(result)
        return results
