import textwrap

from aeug.generation.generator import Generator
from aeug.prompt.prompter import Prompter
from aeug.search.bm25 import BM25
from aeug.utils.typing import CommonSearchOutput

TEMPLATE = textwrap.dedent(
    """\
    Please create five questions that can be considered from the document.
    Only respond with the queries, nothing else.
    Your response should be a list of comma separated values, eg: `foo, bar, baz` or `foo,bar,baz`

    ### Document:
    {}

    ### five queries:
    """
)


class Aeug:
    def __init__(self, model_id: str, benchmark_name: str):
        self.prompter = Prompter(TEMPLATE)
        self.first_step = BM25(benchmark_name)
        self.generator = Generator(model_id)

    def search(self, query, top_k: int = 10):
        first_hits: list[CommonSearchOutput] = self.first_step.search(
            query, top_k
        )
        for hit in first_hits:
            print(hit.content)
            prompt = self.prompter.generate(hit.content)
            queries = self.generator.generate(prompt)
            print(queries)
            break


if __name__ == "__main__":
    # aeug = Aeug("meta-llama/Llama-3.1-70B-Instruct", "trec2020")
    aeug = Aeug("meta-llama/Llama-3.1-8B-Instruct", "trec2020")
    print(aeug.search("What is python proggraming language?"))
