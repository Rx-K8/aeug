import re

from aeug.exceptions import InsufficientQuestionsError
from aeug.logger_config import logger


class Questions:
    def __init__(self, max_size: int = 5):
        self.max_size = max_size
        self.questions: list[str] = []
        self.pattern = r"^[1-5]\.\s*(.*)"

    def add(self, question) -> None:
        if len(self.questions) < self.max_size:
            self.questions.append(question)
            logger.info(f"Question added: {question}")
        else:
            logger.warning(
                f"Max size of questions reached: {self.max_size}. '{question}' was not added."
            )

    def parse(self, text: str) -> list[str]:
        cleaned_text = text.replace("<|eot_id|>", "")
        lines = [
            re.match(self.pattern, line).group(1)
            for line in cleaned_text.strip().split("\n")
            if re.match(self.pattern, line)
        ]
        return lines

    def validate_questions_size(self) -> None:
        if len(self.questions) < 5:
            error_message = (
                f"Number of questions is insufficient: {len(self.questions)}"
            )
            raise InsufficientQuestionsError(error_message)
        else:
            logger.info("Questions are sufficient.")

    def __getitem__(self, index: int) -> str:
        return self.questions[index]

    def __len__(self) -> int:
        return len(self.questions)

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index < len(self.questions):
            question = self.questions[self.iter_index]
            self.iter_index += 1
            return question
        else:
            raise StopIteration

    def __repr__(self) -> str:
        return (
            f"Questions(max_size={self.max_size}, questions={self.questions})"
        )

    @staticmethod
    def from_string(text: str) -> "Questions":
        questions_obj = Questions()
        questions = questions_obj.parse(text)
        for question in questions:
            questions_obj.add(question)

        questions_obj.validate_questions_size()

        return questions_obj


if __name__ == "__main__":
    questions = Questions()
    text = """
1. This is the first line.
2. This is the second line.
3. This is the third line.
4. This is the fourth line.
5. This is the fifth line.
6. This line should not be included.
"""
    try:
        questions = Questions.from_string(text)
    except InsufficientQuestionsError as e:
        logger.exception(e)
