# Findings

## 1. What did you find?

See `alignment.png`: BERT aligns 69% of concatenative words but only 19% of rewritten ones, and GPT-2 drops from 62% to 31%. So once the spelling changes at the join, both tokenizers mostly miss the boundary.

## 2. One example that helped you understand the result

`lazy + ly → lazily`, so the boundary is `lazi|ly`. GPT-2 splits it `l | az | ily`: the rewritten `i` gets glued onto the suffix as the common piece `ily`, so the cut lands one letter early and the boundary is missed.

## 3. One limitation

The metric only counts an exact cut at the boundary, so near misses like `l | az | ily` score the same as a totally random split. For rewritten words it's not even clear where the "right" cut is, since `laz | ily` is arguably just as reasonable as `lazi | ly`.
