from pyserini.search import get_topics
from pyserini.search.lucene import LuceneSearcher

from aeug.io.text import TextWriter
from aeug.search.abc import BaseSearcher
from aeug.utils.convert import CONVERTERS
from aeug.utils.mappings import BM25FLAT_INDEX, TOPICS
from aeug.utils.paths import VALOUTPUT_DIR
from aeug.utils.typing import CommonSearchOutput, ValidationFormat


class BM25(BaseSearcher):
    def __init__(self, benchmark_name: str):
        self.benchmark_name = benchmark_name
        self.topics = get_topics(TOPICS[benchmark_name])
        self.searcher = LuceneSearcher.from_prebuilt_index(
            BM25FLAT_INDEX[benchmark_name]
        )
        self.converter = CONVERTERS[benchmark_name]

    def search(
        self,
        query,
        top_k=1000,
    ) -> list[CommonSearchOutput]:
        hits: list[str] = self.searcher.search(query, top_k)

        format_search_outputs = [
            self.converter.to_common_search_output(
                query=query,
                doc=self.searcher.doc(hit.docid).raw(),
                rank=rank,
                score=hit.score,
            )
            for rank, hit in enumerate(hits, 1)
        ]

        return format_search_outputs

    def to_val_output(
        self,
    ) -> list[ValidationFormat]:
        search_outputs = []
        for topic_id, query in self.topics.items():
            hits = self.search(query["title"])
            for hit in hits:
                search_outputs.append(
                    self.converter.to_val_format(topic_id, hit)
                )
        return search_outputs

    def val(self):
        search_outputs = self.to_val_output()

        outputs = []
        for search_output in search_outputs:
            output = f"{search_output.topic_id} {search_output.q0} {search_output.doc_id} {search_output.rank} {search_output.score: 6f} {search_output.run_tag}"
            outputs.append(output)
        output_file = VALOUTPUT_DIR / f"{self.benchmark_name}.txt"
        TextWriter(output_file).write(outputs)


if __name__ == "__main__":
    # bm25 = BM25("beir_trec_covid")
    bm25 = BM25("trec2020")
    hits = bm25.val()
