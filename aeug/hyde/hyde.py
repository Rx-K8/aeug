from aeug.generation.generator import Generator
from aeug.prompt.prompter import Prompter

TEMPLATE = """Please write a passage to answer the question.
Question:{}
Passage:"""


class Hyde:
    def __init__(self, model_id: str) -> None:
        self.prompter = Prompter(TEMPLATE)
        self.generator = Generator(model_id)
        # self.encoder = encoder
        # self.searcher = searcher

    def prompt(self, query):
        return self.prompter.generate(query)

    def generate(self, query):
        prompt = self.prompt(query)
        return self.generator.generate(prompt)

    def search(self, query):
        pass


if __name__ == "__main__":
    # hyde = Hyde("meta-llama/Meta-Llama-3.1-8B-Instruct")
    hyde = Hyde("meta-llama/Llama-3.2-1B")
    output = hyde.generate("What is the capital of France?")
    print(output)
