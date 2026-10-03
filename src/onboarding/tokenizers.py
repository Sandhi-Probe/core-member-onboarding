"""Small helpers for inspecting Hugging Face tokenizer outputs."""

from __future__ import annotations

from transformers import AutoTokenizer, PreTrainedTokenizerBase


DEFAULT_TOKENIZERS = {
    "bert": "bert-base-uncased",
    "gpt2": "gpt2",
}


def load_tokenizers(model_names: dict[str, str] | None = None):
    """Load fast tokenizers so that offset mappings are available."""
    names = model_names or DEFAULT_TOKENIZERS
    return {
        label: AutoTokenizer.from_pretrained(model_name, use_fast=True)
        for label, model_name in names.items()
    }


def tokenize_with_offsets(
    tokenizer: PreTrainedTokenizerBase,
    text: str,
) -> dict:
    """Return human-readable tokens together with character offsets."""
    encoded = tokenizer(
        text,
        add_special_tokens=False,
        return_offsets_mapping=True,
    )

    return {
        "input_ids": encoded["input_ids"],
        "tokens": tokenizer.convert_ids_to_tokens(encoded["input_ids"]),
        "offsets": [tuple(pair) for pair in encoded["offset_mapping"]],
    }
