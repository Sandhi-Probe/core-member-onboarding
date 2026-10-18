# Findings

## 1. What did you find?

Both tokenizers were noticeably worse at identifying suffix boundaries when the spelling changed. BERT went from around 69% alignment for concatenative words to 19% for rewritten words, while GPT-2 went from 62% to 31%.

What's interesting is that BERT did better than GPT-2 on concatenative words, but GPT-2 did better on rewritten words. Overall, the results suggest that spelling changes make it harder for tokenizers to split words at the correct morphological boundary.

## 2. One example that helped you understand the result

One example is "lazily", which comes from "lazy + ly", where the "y" changes to "i". GPT-2 split it into `['l', 'az', 'ily']`, even though the actual suffix starts at "ly".

So even though the tokenizer split the word into three pieces, none of those splits lined up with where the suffix starts.

## 3. One limitation

One issue is that words represented as a single token automatically count as misaligned, since there's no split to begin with. This could affect the results because we're not just measuring whether tokenizers recognize suffix boundaries, but also how often they split words in general.

Also, the way we're classifying rewritten words is pretty simplistic, so some words might end up in the wrong group.