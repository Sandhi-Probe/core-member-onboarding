# Findings

## 1. What did you find?

Yes. Both tokenizers miss the suffix boundary a lot more when the spelling changes at the join (see `alignment.png`):

- BERT: 69% aligned for normal words, 19% for rewritten words
- GPT-2: 62% aligned for normal words, 31% for rewritten words

Rewritten words don't get split into many more pieces (BERT 3.0 vs 2.7 tokens, GPT-2 3.1 vs 3.1). The cuts just land in the wrong place. This is one sample of 500 words per group, so I trust the big gap more than the exact numbers.

## 2. One example that helped you understand the result

`clarifiable` = clarify + able. The "y" becomes "i", so the suffix starts at position 7 (`clarifi|able`).

GPT-2 splits it `cl | ar | ifiable`. It has `ifiable` as one token, so the changed "i" gets glued onto the suffix and no token starts at 7. That's a miss.

## 3. One limitation

The "rewritten" group isn't only spelling changes. Anything that isn't exactly source + suffix gets labeled rewritten, so it also picks up words with a different history, like bottle + er → `butler`, bite + le → `beetle`, and Neil + son → `Nelson`. Those aren't spelling rules at the join. So the rewritten group is noisy, and this experiment can't say the spelling change itself is what causes the misses.
