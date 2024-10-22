class Prompter:
    def __init__(self, template: str) -> None:
        self.template = template

    def generate(self, query) -> str:
        return self.template.format(query)
