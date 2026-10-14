# Findings

## 1. What did you find?

It appears that the BERT tokenizer aligns 69.2% of concatenative words and only 18.8% of rewritten ones. GPT-2 presented a similar pattern, aligning 62.2% of concatenative words and only 31.4% of rewritten ones. This suggests that both tokenizers are significantly less likely to align tokens correctly when the boundary involves a spelling change, meaning rewritten words pose a significant barrier to accurately identifying and tokenizing the morpheme boundaries (in this experiment).

## 2. One example that helped you understand the result

The word clarifiable looks like a classic rewritten example where `clarify + able → clarifiable`. However, in our results, we see that GPT-2 splits it into cl, ar, and ifiable - `cl|ar|ifiable`. The suffix morpheme -able is attached onto the preceding part of the word. Thus, the boundary is missed by the tokenizer, which marks it two places before where the split should actually be.

## 3. One limitation

Throughout this experiment, I've found that it was quite hard to guage what is actually correct. For example, between `marbl|y` and `marb|ly`, which one would be the correct split? Currently I would just assume, based on English conventions, that the one with the -ly token is "more" correct. However, this isn't explicitly defined in the experiment, so there is no way to say for sure whether tokenizers split words at the "right" place. With this ambiguity, there can also easily be cases where a word is misclassified. For example in the previous case, if was accept `marb|ly` as a valid tokenization, it could be classified as a concatenation by accident instead of a rewritten word (`marb + ly -> marbly`). This could skew results in favour of concatenative words unintentionally.
