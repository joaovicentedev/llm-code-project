"""Local Hugging Face adapter for Qwen3-0.6B."""

from functools import lru_cache

from prompt import PROMPT


MODEL_ID = "Qwen/Qwen3-0.6B"


class QwenLLM:
    def __init__(self, model_id: str = MODEL_ID) -> None:
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id)
        self.model.eval()

    def generate(self, user_message: str, max_new_tokens: int = 256) -> str:
        import torch

        messages = [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": user_message},
        ]
        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            enable_thinking=False,
            return_tensors="pt",
            return_dict=True,
        )
        with torch.inference_mode():
            output = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
            )
        generated_tokens = output[0][inputs["input_ids"].shape[-1] :]
        return self.tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()


@lru_cache(maxsize=1)
def get_llm() -> QwenLLM:
    return QwenLLM()
