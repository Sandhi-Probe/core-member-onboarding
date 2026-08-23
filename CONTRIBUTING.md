# Contributing

This repository is designed around a simple onboarding workflow: make a small research contribution, open a PR, receive feedback, and revise it.

## 1. Create a branch

Use a branch named:

```text
onboarding/<github-username>
```

Example:

```bash
git checkout -b onboarding/alex-example
```

## 2. Keep your changes scoped

Your PR should mainly add one self-contained directory:

```text
submissions/<github-username>/
├── analysis.ipynb   # or an equivalent script
├── findings.md
└── results/
    └── <your figure(s)>
```

Do not edit another contributor's submission directory.

Avoid committing:

- the full MorphyNet dataset;
- model weights or Hugging Face caches;
- virtual environments;
- large generated artifacts unrelated to the final analysis.

## 3. Before opening the PR

Check that:

- the notebook runs top-to-bottom from a fresh kernel;
- random sampling uses a fixed seed;
- tokenizer/model names are recorded;
- at least one result figure or table is included;
- `findings.md` explains the result and a limitation;
- temporary debugging cells/files are removed.

## 4. Open the PR

Push your branch and open a pull request into `main`.

Use the provided PR template. A reviewer will leave feedback directly on the PR. Respond to the feedback with additional commits rather than opening a new PR.

## Asking for help

Getting stuck is expected during onboarding. When asking for help, include:

1. what you were trying to do;
2. what you expected;
3. what happened instead;
4. the smallest relevant code/error snippet.

Research work is collaborative; asking a precise question is a useful skill, not a failure mode.
