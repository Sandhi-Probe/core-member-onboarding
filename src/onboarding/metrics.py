"""Metric stubs for the onboarding experiment.

Participants should implement the TODOs as part of the project.
"""

from __future__ import annotations


def boundary_aligned(offsets: list[tuple[int, int]], boundary: int) -> bool:
    """Return True if a token begins at the gold suffix boundary.

    TODO: implement this function.

    Hint: inspect the start position of each tokenizer offset. Think about
    whether position 0 or zero-length offsets need special handling.
    """
    raise NotImplementedError("Implement boundary_aligned as part of onboarding")


def tokens_per_word(input_ids: list[int]) -> int:
    """Simple fragmentation metric: number of non-special tokens for a word."""
    return len(input_ids)
