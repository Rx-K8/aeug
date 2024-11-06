import textwrap

from transformers import AutoModel, AutoTokenizer

from aeug.contriever import Contriever
from aeug.generation.generator import Generator
from aeug.logger_config import logger
from aeug.outputs.questios import Questions
from aeug.prompt.prompter import Prompter
from aeug.search.bm25 import BM25
from aeug.utils.typing import CommonSearchOutput

TEMPLATE = textwrap.dedent(
    """\
    Please create five questions that can be considered from the document.
    Please output as a numbered list.
    Only respond with the queries, nothing else.

    ### Document:
    {}

    ### Five questions:
    """
)


class Aeug:
    def __init__(self, model_id: str, benchmark_name: str):
        self.prompter = Prompter(TEMPLATE)
        self.first_step = BM25(benchmark_name)
        self.generator = Generator(model_id)
        self.contriever = Contriever()

    def similarity(self, query: str, content: str):
        score = self.contriever.dot_score(query, content)
        return score

    def search(self, query, top_k: int = 5):
        first_hits: list[CommonSearchOutput] = self.first_step.search(
            query, top_k
        )
        for hit in first_hits:
            prompt = self.prompter.generate(hit.content)
            output = self.generator.generate(prompt)
            try:
                questions = Questions.from_string(output)
            except Exception as e:
                logger.exception(e)

            max_score = (None, -float("inf"))
            for i, question in enumerate(questions):
                question_score = self.similarity(query, question)
                if max_score[1] < question_score:
                    max_score = (i, question_score)
                hit.score = max_score[1]
        sorted_hits = sorted(first_hits, key=lambda x: x.score, reverse=True)
        for i, hit in enumerate(sorted_hits):
            hit.rank = i + 1

        return sorted_hits





if __name__ == "__main__":
    # aeug = Aeug("meta-llama/Llama-3.1-70B-Instruct", "trec2020")
    # aeug = Aeug("meta-llama/Llama-3.1-8B-Instruct", "trec2020")
    # aeug = Aeug(
    #     "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4", "trec2020"
    # )
    aeug = Aeug(
        "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "trec2020"
    )
    print(aeug.search("What is python proggraming language?"))
