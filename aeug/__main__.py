import sys

from pyserini.search import get_qrels, get_topics
from tqdm import tqdm

from aeug.hyde.hyde import Hyde
from aeug.io.jsonl import JsonlWriter


def main():
    model_id = "meta-llama/Llama-3.1-70B-Instruct"
    hyde = Hyde(model_id)
    topics = get_topics("dl19-passage")
    qrels = get_qrels("dl19-passage")

    results = []
    for qid in tqdm(topics):
        if qid in qrels:
            query = topics[qid]["title"]
            hits = hyde.search(query)

            rank = 0
            for hit in hits:
                rank += 1
                result = f"{qid} Q0 {hit.docid} {rank} {hit.score} rank"
                results.append(result)
    JsonlWriter("results.jsonl", results).write()

    return 0


if __name__ == "__main__":
    sys.exit(main())
