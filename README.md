# Tokenizers & English Morphology — Week 1 Onboarding

A beginner-friendly research onboarding project for exploring a simple question:

> **Do common tokenizers preserve English morphological boundaries less reliably when word formation changes the spelling of the stem?**

This is a small English analogue of our larger research theme: studying cases where an underlying linguistic boundary exists, but the surface characters around that boundary are changed or obscured.

## What you will learn

By the end of this onboarding project, you should have practiced:

- loading and filtering a real morphology dataset;
- using Hugging Face tokenizers;
- inspecting token IDs, token strings, and character offsets;
- defining a simple quantitative metric;
- comparing experimental groups;
- visualizing and interpreting results;
- communicating research work through a GitHub pull request.

No prior linguistics knowledge is expected. No GPU is required.

## Dataset

We use **MorphyNet**, a multilingual morphology database. The English derivational file contains relationships such as a source word, derived target word, morpheme, and whether that morpheme is a prefix or suffix.

Upstream repository:
https://github.com/kbatsuren/MorphyNet

English derivational data:
https://github.com/kbatsuren/MorphyNet/blob/main/eng/eng.derivational.v1.tsv

The starter loader downloads the dataset automatically. **Do not commit the full dataset to this repository.**

MorphyNet is distributed under CC BY-SA 3.0; see the upstream repository for details.

## The idea

Compare two types of suffixation.

### Boundary-preserving

The target is simple concatenation:

```text
slow + ly -> slowly
use + less -> useless
```

### Boundary-rewriting

The derived word is not simply `source + suffix`:

```text
happy + ness -> happiness
```

The second group is an English approximation of the phenomenon we care about in the main project: the linguistic relationship is still present, but the surface form around the boundary has changed.

## Your task

Use the provided starter notebook and utilities to answer:

> **Are tokenizer boundaries less likely to align with suffix boundaries in rewritten words than in simple concatenative words?**

### Required experiment

1. Load the English MorphyNet derivational dataset.
2. Keep suffix examples and apply reasonable cleaning/filtering.
3. Label examples as:
   - `concatenative`: `target == source + morpheme`
   - `rewritten`: `target != source + morpheme`
4. Sample a manageable, reasonably balanced subset from both groups.
5. Compare **at least two Hugging Face tokenizers**. Suggested starting pair:
   - `bert-base-uncased`
   - `gpt2`
6. Define and compute at least **two metrics**. One must be morphological boundary alignment. A second can be:
   - tokens per word;
   - token count change from source to target;
   - stem token preservation;
   - another metric you motivate.
7. Create at least **one useful plot or table** comparing the two groups.
8. Write a short interpretation of what you found.

## Morphological boundary alignment

For a suffix derivation where the target ends with the listed morpheme, the suffix starts at:

```python
boundary = len(target) - len(morpheme)
```

Using tokenizer offset mappings, ask whether a token starts at that character position.

For example, if the true morphology is:

```text
slow | ly
```

then a tokenization that places a token boundary between `slow` and `ly` counts as aligned.

The starter utilities show you how to get character offsets. You are responsible for implementing and validating the alignment metric.

## Deliverables

Your PR should contain:

- a directory at `submissions/<github-username>/` containing:
  - your completed `analysis.ipynb` **or** equivalent analysis script;
  - at least one figure under `results/`;
  - a short `findings.md` containing:
  - your methodology;
  - your main result(s);
  - one limitation;
  - one follow-up experiment you would try.

Please keep the project small. A clear experiment with a thoughtful interpretation is more valuable than adding many models or complicated methods.

## Suggested one-week pacing

You do not need to follow this exactly.

**Part 1 — Setup and exploration:** Clone the repo, create an environment, run the starter notebook, and inspect MorphyNet examples.

**Part 2 — Tokenizer exploration:** Learn how your two tokenizers split words and how offset mappings work.

**Part 3 — Core experiment:** Implement boundary alignment and one additional metric, then run the comparison.

**Part 4 — Analysis:** Make a plot/table, inspect surprising examples, and write down what the results do and do not show.

**Part 5 — PR and revision:** Open your PR, respond to review feedback, and revise your work.

## Optional stretch goals

Choose at most one if the core experiment is complete.

- Create a continuous spelling-change / boundary-destruction score using edit distance.
- Compare more tokenizer families.
- Break rewritten examples into rough spelling-change categories.
- Investigate whether word frequency or word length explains part of the effect.
- Manually inspect failure cases and propose a better metric.

## What we care about in review

We are **not** looking for a predetermined conclusion. A null or unexpected result is completely acceptable.

We will mainly review:

- whether the experiment matches the stated question;
- whether the metric is implemented correctly;
- whether comparisons are fair and reproducible;
- whether plots/tables are understandable;
- whether conclusions match the evidence;
- whether limitations are recognized;
- whether the code and PR are easy for another teammate to follow.

## Getting started

```bash
git clone <REPO_URL>
cd tokenizer-morphology-onboarding
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then open `starter/onboarding.ipynb`. Before you begin your final analysis, create your own submission folder:

```bash
mkdir -p submissions/<github-username>/results
cp starter/onboarding.ipynb submissions/<github-username>/analysis.ipynb
cp findings_template.md submissions/<github-username>/findings.md
```

Work in your copy under `submissions/`, not in the shared starter notebook.

See `CONTRIBUTING.md` before opening your PR.
