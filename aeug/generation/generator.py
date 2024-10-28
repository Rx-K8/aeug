from abc import ABC

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


class GeneratorBase(ABC):
    def __init__(self, model_id: str, max_length: int) -> None:
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(model_id).to(
            self.device
        )
        self.max_length = max_length


class Generator(GeneratorBase):
    def __init__(self, model_id: str, max_length: int = 1000) -> None:
        super().__init__(model_id, max_length)

    def generate(self, prompt) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = inputs.to(self.device)
        generate_ids = self.model.generate(
            inputs.input_ids, max_length=self.max_length
        )
        output = self.tokenizer.batch_decode(generate_ids)

        return output
