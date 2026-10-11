# Findings

## 1. What did you find?

See `alignment.png`: BERT aligns 69% of concatenative words but only 19% of rewritten ones, and GPT-2 drops from 62% to 31%. So once the spelling changes at the join, both tokenizers mostly miss the boundary.

## 2. One example that helped you understand the result

`lazy + ly → lazily`, so the boundary is `lazi|ly`. GPT-2 splits it `l | az | ily`: the rewritten `i` gets glued onto the suffix as the common piece `ily`, so the cut lands one letter early and the boundary is missed.

## 3. One limitation

The metric only counts an exact cut at the boundary, so near misses like `l | az | ily` score the same as a totally random split. For rewritten words it's not even clear where the "right" cut is, since `laz | ily` is arguably just as reasonable as `lazi | ly`.

## Bonus: dropping single-token words

A single-token word can never align, since its only token starts at position 0. Dropping those words barely moves anything: BERT goes from 69% vs 19% to 71% vs 20%, and GPT-2 goes from 62% vs 31% to 62% vs 32%. Single-token words are rare (47 of BERT's 1,000 words, 5 of GPT-2's), so the gap comes from multi-token words cut in the wrong place, not from whole-word tokens.

## Bonus: adding Qwen

`Qwen/Qwen2.5-0.5B`'s tokenizer lands right next to GPT-2: 64% for concatenative vs 32% for rewritten (GPT-2: 62% vs 31%). Makes sense, since both use BPE (BERT uses WordPiece), and Qwen's 3x bigger vocab (151,665 vs 50,257) still makes the same cuts on these words (`l | az | ily`, `stuff | ily`). The last code cell in the notebook prints all of this.
