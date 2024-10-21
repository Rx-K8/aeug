from string import Template


class Prompter:
    def __init__(self, template: str) -> None:
        self.template: Template = Template(template)
        print(type(self.template))
        print(self.template)

    def generate(self, query) -> str:
        return self.template.substitute(query=query)
