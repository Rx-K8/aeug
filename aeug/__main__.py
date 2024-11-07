import sys

from pyserini.search import get_qrels, get_topics
from tqdm import tqdm

from aeug.io.jsonl import JsonlWriter
from aeug.io.text import TextWriter
from aeug.paths import VALOUTPUT_DIR

# from aeug.hyde.hyde import Hyde
from aeug.search.aeug_search import Aeug
from aeug.utils.mappings import TOPICS
from aeug.utils.typing import ValidationFormat


def main():
    # model_id = "meta-llama/Llama-3.1-70B-Instruct"
    # hyde = Hyde(model_id)
    bench_mark = "trec2020"
    aeug = Aeug(
        "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", bench_mark
    )
    topics = get_topics(TOPICS[bench_mark])
    qrels = get_qrels(TOPICS[bench_mark])

    results = []
    for qid in tqdm(topics):
        if qid in qrels:
            query = topics[qid]["title"]
            hits = aeug.search(query, 500)

            rank = 0
            for hit in hits:
                rank += 1

                result = f"{qid} Q0 {hit.doc_id} {rank} {hit.score} rank"
                results.append(result)
    # JsonlWriter("results.jsonl", results).write()
    output_file = VALOUTPUT_DIR / "trec2020_aeug.txt"
    TextWriter(output_file).write(results)

    return 0


if __name__ == "__main__":
    sys.exit(main())
