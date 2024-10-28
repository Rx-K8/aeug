import textwrap

import numpy as np
from pyserini.search.faiss import AutoQueryEncoder

from aeug.generation.generator import Generator
from aeug.io.json import JsonWriter
from aeug.prompt.prompter import Prompter
from aeug.search.searcher import VectorSearcher
from aeug.utils.typing import PathLike, Results

TEMPLATE = textwrap.dedent(
    """\
    Please write a passage to answer the question.
    Question:{}
    Passage:"""
)


class Hyde:
    def __init__(self, model_id: str) -> None:
        self.prompter = Prompter(TEMPLATE)
        self.generator = Generator(model_id)
        self.encoder = AutoQueryEncoder(
            encoder_dir="facebook/contriever", pooling="mean"
        )
        self.searcher = VectorSearcher("facebook/contriever")

    def encode(self, query, hypothesis_documents):
        all_emb_c = []
        for c in [query] + hypothesis_documents:
            c_emb = self.encoder.encode(c)
            all_emb_c.append(np.array(c_emb))
        all_emb_c = np.array(all_emb_c)
        avg_emb_c = np.mean(all_emb_c, axis=0)
        hyde_vector = avg_emb_c.reshape((1, len(avg_emb_c)))
        return hyde_vector

    def prompt(self, query):
        return self.prompter.generate(query)

    def generate(self, query):
        prompt = self.prompt(query)
        return self.generator.generate(prompt)

    def search(self, query):
        hypothesis_documents = self.generator.generate(query)
        vector = self.encode(query, hypothesis_documents)
        hits = self.searcher.search(vector)
        # hits = self.searcher.get_documents(vector)
        return hits

    def write(self, data: Results, output_file: PathLike):
        JsonWriter(output_file, data).write()

    @staticmethod
    def default():
        model_id = "facebook/contriever"
        return Hyde(model_id)
