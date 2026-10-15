# Findings

## 1. What did you find?

Yes, the boundary gets missed a lot more when the spelling changes. With 500 words per group, the alignment rates were:

| tokenizer | concatenative | rewritten |
|-----------|---------------|-----------|
| bert      | 0.692         | 0.188     |
| gpt2      | 0.622         | 0.314     |

So for both tokenizers the rewritten words are aligned way less often. The gap is bigger for BERT (about 50 points) than for GPT-2 (about 31 points). Rewritten words also used a few more tokens on average for BERT (3.02 vs 2.70), but for GPT-2 it was basically the same (3.09 vs 3.06). I only ran one sample, so I wouldn't trust the exact numbers too much, but the gap is big enough that it doesn't look like noise.

## 2. One example that helped you understand the result

`happiness` (happy + ness, the y turns into i). The suffix starts at character 5. BERT keeps it as one token, `['happiness']`, so there's no boundary at all. GPT-2 splits it as `['h', 'appiness']`, so the split is at position 1, which is nowhere near the real boundary. Compare that to `slowly`, where GPT-2 gives `['slow', 'ly']` and gets it exactly right. What surprised me is that the tokenizers aren't looking at morphemes at all. They just split on what's common in their training text, and that only lines up with the suffix when the word is spelled "normally".

## 3. One limitation

The `rewritten` label comes from a simple rule (target != source + suffix), so it isn't clean. For example `rodomontade + er -> rhodomontader` is labeled rewritten, but it looks like a spelling variant or typo in the data, not a real spelling change at the join. Also, some words are a single token (like `retired` in BERT), and those can never count as aligned, so part of the gap could just be common words being kept whole. Because of this, the experiment shows that rewritten words are missed more often, but not that the spelling change itself is the cause.
