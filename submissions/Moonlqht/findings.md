# Findings

## 1. What did you find?

Give the alignment rate for each group and tokenizer (or point to your plot), and say in one or two sentences what the numbers suggest.

In general, the concatenative group had a much higher alignment rate than the rewritten group. GPT2 is better with rewritten groups, whereas bert is better with concatenative. 

Bert has a concatenative score of 0.692, rewritten of 0.188. 
GPT2 has a concatenative score of 0.622, rewritten of 0.314. 

## 2. One example that helped you understand the result

Pick a word and show how a tokenizer split it.

muffled with GPT2 is split as:

m, uff, led

In the english language, should likely be muffle + ed. 

## 3. One limitation

Give one reason this experiment doesn't fully answer the question.

Words that aren't boundary aligned doesn't always mean that they're split wrong. It could just be that they're not split, and our code doesn't particularly account for this. 

Also, there can be several ways to split a word. For example, the -ed suffix is pretty common (for example, muffled). The "correct" splitting here could be muffle + d, or muffl + ed. Both logically work, but there can only be one correct answer. 