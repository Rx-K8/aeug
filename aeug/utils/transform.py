from aeug.utils.typing import Results


def transform_result(docs) -> Results:
    return [
        {
            "query_id": doc["query_id"],
            "query": doc["query"],
            "rank": doc["rank"],
            "score": doc["score"],
        }
        for doc in docs
    ]
