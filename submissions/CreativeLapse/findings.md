# Findings

## 1. What did you find?

After looking at the data, it seems that boundary alignment is much lower when the forms are rewritten. BERT aligned 0.709 of words in the concatenative group, and 0.202 for rewritten. GPT-2 got 0.623 concatenative vs 0.317 rewritten. While both have a drop in performance, BERT’s seems more exaggerated. These results indicate that when adding a suffix changes the spelling of the word, tokenizers are much worse at placing a token boundary accurately (at the suffix boundary). This is the same across BERT and GPT-2, although the magnitude of the disparity varies. Qwen2.5 performs almost the exact same as GPT-2, which is likely because of using the same tokenizer algorithm and training on similar English data. 

## 2. One example that helped you understand the result

For example, “lazily”. The suffix boundary is at “lazi”, so =4. GPT-2 splits it as  ['l', 'az', 'ily'], the offsets being (0,1),(1,3),(3,6). Since no token starts at 4, the boundary is not aligned. BERT splits it with offsets (0,2),(2,6) which again misses the boundary at 4. This example shows how the join point is usually within a token when the spelling is rewritten instead of concatenative. 

## 3. One limitation

For one, labelling a word as ‘rewritten’ is done by a simple algorithm seeing if the target is equal to the source + the morpheme. This makes some assumptions which could cause false rewritten cases, like “making”. “Making” has an e that is dropped, the suffix “ing” did not change in spelling, but the base word changed so the rewritten algorithmic check would falsely return that this word is rewritten. Also, words that are tokenized into one token can’t be aligned at a suffix boundary at all, so common words in training data not being split at all would be counted as failures even though the word was understood. However, this problem is fixed by the bonus only taking results for multi-token words.
