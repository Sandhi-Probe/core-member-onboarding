# Findings

## 1. What did you find?

> "Give the alignment rate for each group and tokenizer (or point to your plot), and say in one or two sentences what the numbers suggest."

For both tokenizers, the alignment rate for `concatenative` is much higher than `rewritten`: 0.692 vs 0.188 for `bert`, and 0.622 vs 0.314 for `gpt2`. I believe this means when adding the suffix changes the spelling (`rewritten`) it is much less likely that the morpheme (suffix) is correctly isolated by the tokenizer as an individual token.

## 2. One example that helped you understand the result

> "Pick a word and show how a tokenizer split it."

"relaxedness" was tokenized into [rel, ax, ed, ness] by gpt2. In this situation "ness" is a morpheme, which is aligned (i.e. is its individual token), so aligned=True for this example. 

## 3. One limitation

> "Give one reason this experiment doesn't fully answer the question."

The original question is "do tokenizers split words at the right place less often when adding a suffix changes the spelling".

I think "at the right place“ is a subjective thing that we've not fully defined yet. At this point we haven't shown that splitting words at the morpheme is necessarily more correct, or that NOT splitting words at the morpheme leads to incorrectness downstream, etc.

## optional observations

### single-token words

`bert` tokenizes more words into single-tokens than `gpt2`. 

Also, more words in `rewritten` are single-token words than in `concatenative`. 

The general trend remains the same. as a sanity check, n_tokens goes up for each category since one-token words were removed, increasing the mean.

### Extra tokenizer

Qwen2.5-0.5b's tokenizer was added. The same patterns hold. 

Observation: Qwen tokenizes words very similarly to gpt2

Full results:

|tokenizer|group|aligned|n_tokens
|-|-|-|-|
|bert|concatenative|0.692|2.704|
||rewritten|0.188|3.024|
|gpt2|concatenative|0.622|3.064|
||rewritten|0.314|3.090|
|qwen|concatenative|0.636|2.950|
||rewritten|0.318|2.956|

With one-token words removed:

|tokenizer|group|aligned|n_tokens
|-|-|-|-|
|bert|concatenative|0.709|2.746|
||rewritten|0.202|3.176|
|gpt2|concatenative|0.623|3.068|
||rewritten|0.317|3.107|
|qwen|concatenative|0.636|2.950|
||rewritten|0.323|2.984|