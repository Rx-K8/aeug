from abc import ABC

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AwqConfig


class GeneratorBase(ABC):
    def __init__(self, model_id: str, max_new_tokens: int) -> None:
        self.model_id = model_id
        # self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # self.device = "auto"
        self.quantization_config = AwqConfig(
            bits=4,
            fuse_max_seq_len=512,  # Note: Update this as per your use-case
            do_fuse=True,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            device_map="auto",
            quantization_config=self.quantization_config,
        )
        self.max_new_tokens = max_new_tokens


class Generator(GeneratorBase):
    def __init__(self, model_id: str, max_new_tokens: int = 200) -> None:
        super().__init__(model_id, max_new_tokens)

    def generate(self, prompt) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = inputs.to("cuda")
        generate_ids = self.model.generate(
            **inputs,
            pad_token_id=self.tokenizer.eos_token_id,
            max_new_tokens=self.max_new_tokens,
        )
        output = self.tokenizer.batch_decode(generate_ids)

        return output[0]
