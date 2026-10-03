# Tokenizers & English Morphology — Onboarding Task

**Time:** about 3–4 hours. **Due:** before our second team meeting.

## The question

> **Do tokenizers split words at the right place less often when adding a suffix changes the spelling?**

Some words are built by simple concatenation:

```text
slow + ly  -> slowly       (boundary survives: slow | ly)
```

Others change spelling at the join:

```text
happy + ness -> happiness  (the "y" became "i")
```

This is a small English version of our main project: in Sanskrit sandhi, the characters at a word boundary get rewritten (`rāma + iti → rāmeti`). Here you'll measure whether that kind of change makes tokenizers miss the boundary.

No linguistics background or GPU needed.

## Setup

```bash
git clone https://github.com/Sandhi-Probe/core-member-onboarding.git
cd core-member-onboarding
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Make your own branch and submission folder (replace `<username>` with your GitHub username):

```bash
git checkout -b onboarding/<username>
mkdir -p submissions/<username>
cp starter/onboarding.ipynb submissions/<username>/analysis.ipynb
cp findings_template.md submissions/<username>/findings.md
```

Open `submissions/<username>/analysis.ipynb` in Jupyter (`jupyter lab`) or VS Code.

## The task

The notebook loads the data and tokenizers for you. You fill in three small `TODO`s:

1. **Implement `boundary_aligned`**: does a token start exactly where the suffix starts? The notebook has checks that pass once it's right.
2. **Fill in the experiment loop**: record, for each word and tokenizer, whether the boundary aligned and how many tokens it used.
3. **Make one plot** comparing the two groups. The notebook saves it as `alignment.png`.

Then fill in `findings.md`: three short answers, a few sentences each.

A null or surprising result is fine. We care that the code is correct and the conclusion matches the evidence.

## Submitting

Your PR should only add files under `submissions/<username>/`:

```text
submissions/<username>/
├── analysis.ipynb
├── findings.md
└── alignment.png
```

```bash
git add submissions/<username>
git commit -m "Onboarding: <your name>"
git push -u origin onboarding/<username>
```

Open a pull request into `main` on GitHub. A TPM will review it; reply to comments by pushing more commits to the same branch.

Can't push? Ask a TPM on Discord to add you to the GitHub org.

## Optional (only if you're done and curious)

- Some words are a single token, so they can never "align." Drop them and check whether the gap between groups changes.
- Add a third tokenizer, e.g. `Qwen/Qwen2.5-0.5B`.

## Getting help

Stuck is normal. Post in Discord with what you tried, what you expected, what happened, and the error message.

---

Data: English derivational file from [MorphyNet](https://github.com/kbatsuren/MorphyNet) (CC BY-SA 3.0). The notebook downloads it automatically; don't commit it.
