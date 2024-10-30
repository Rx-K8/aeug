import textwrap

from aeug.prompter import Prompter

TEMPLATE = textwrap.dedent(
    """\
    Please create questions that can be considered from the document.
    Only respond with the queries, nothing else.
    Your response should be a list of comma separated values, eg: `foo, bar, baz` or `foo,bar,baz`

    ### Document:
    {}

    ### queries:
    """
)


class Aeug:
    def __init__(self):
        self.prompter = Prompter(TEMPLATE)


if __name__ == "__main__":
    aeug = Aeug()
    print(aeug.prompter.generate("This is a test document."))
