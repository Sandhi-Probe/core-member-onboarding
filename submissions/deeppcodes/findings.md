# Findings

## 1. What did you find?

Give the alignment rate for each group and tokenizer (or point to your plot), and say in one or two sentences what the numbers suggest.

Stats:
BERT: concatenative 69.2% aligned vs rewritten 18.8%
GPT-2: concatenative 62.2% vs rewritten 31.4%

- When the suffix changes the spelling, both tokenizers often miss the boundary
- The gap is bigger for BERT compared to GPT-2 
- Reference: core-member-onboarding/submissions/deeppcodes/alignment.png

## 2. One example that helped you understand the result

Word: lazily, Tokenizer: GPT-2 [l, az, ily]
- lazy + ly -> lazily. The y became i
- the suffix "ly" starts at position 4, so the boundary is 4
- the tokens start at 0, 1, 3, so it's a miss
- GPT-2 put the changed "i" together with the suffix ("ily"), so the spelling change moved the cut one letter to the left


## 3. One limitation

The experiment only checks one boundary per word. But some words have more than one real boundary, and a tokenizer can split at a different one and still get counted as a miss

Word: authorizer, Tokenizer: BERT [author, ##izer]
- authorize + er -> authorizer. The boundary is 8 (authoriz|er)
- The tokens start at 0 and 6 so the experiment counts it as not aligned
- But the tokenizer did split at a real word part: author|izer (author+ize)
- Some misses arent really the tokenizer ignoring word structure, its maybe picking a different part of the word.
