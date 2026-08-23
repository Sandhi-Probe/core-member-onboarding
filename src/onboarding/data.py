"""MorphyNet loading and lightweight preprocessing helpers."""

from __future__ import annotations

import pandas as pd

MORPHYNET_ENGLISH_DERIVATIONAL_URL = (
    "https://raw.githubusercontent.com/kbatsuren/MorphyNet/"
    "main/eng/eng.derivational.v1.tsv"
)

# MorphyNet's derivational schema, as documented in the upstream README.
COLUMNS = [
    "source",
    "target",
    "source_pos",
    "target_pos",
    "morpheme",
    "affix_type",
]


def load_morphynet(url: str = MORPHYNET_ENGLISH_DERIVATIONAL_URL) -> pd.DataFrame:
    """Load the English MorphyNet derivational file.

    The upstream per-language TSV is read without assuming a header row.
    """
    df = pd.read_csv(
        url,
        sep="\t",
        header=None,
        names=COLUMNS,
        dtype=str,
        keep_default_na=False,
    )

    # Be defensive in case an upstream version ever includes a header-like row.
    if not df.empty and str(df.iloc[0]["source"]).strip().lower() in {
        "source",
        "source word",
        "source_word",
    }:
        df = df.iloc[1:].copy()

    return df.reset_index(drop=True)


def prepare_suffix_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a beginner-friendly subset for the onboarding experiment.

    We keep alphabetic English suffix derivations whose target visibly ends in
    the listed suffix. This makes the target-side suffix boundary well-defined.
    """
    work = df.copy()

    for col in ["source", "target", "morpheme", "affix_type"]:
        work[col] = work[col].astype(str).str.strip()

    work = work[work["affix_type"].str.lower() == "suffix"].copy()
    work = work[
        work["source"].str.fullmatch(r"[A-Za-z]+", na=False)
        & work["target"].str.fullmatch(r"[A-Za-z]+", na=False)
        & work["morpheme"].str.fullmatch(r"[A-Za-z]+", na=False)
    ].copy()

    work = work[
        work.apply(lambda row: row["target"].lower().endswith(row["morpheme"].lower()), axis=1)
    ].copy()

    work["concatenative_target"] = work["source"] + work["morpheme"]
    work["group"] = work.apply(
        lambda row: (
            "concatenative"
            if row["target"].lower() == row["concatenative_target"].lower()
            else "rewritten"
        ),
        axis=1,
    )
    work["suffix_boundary"] = work.apply(
        lambda row: len(row["target"]) - len(row["morpheme"]), axis=1
    )

    return work.reset_index(drop=True)


def balanced_sample(
    df: pd.DataFrame,
    n_per_group: int = 500,
    random_state: int = 42,
) -> pd.DataFrame:
    """Sample up to ``n_per_group`` rows from each experiment group."""
    pieces = []
    for group in ["concatenative", "rewritten"]:
        group_df = df[df["group"] == group]
        n = min(n_per_group, len(group_df))
        pieces.append(group_df.sample(n=n, random_state=random_state))

    return (
        pd.concat(pieces, ignore_index=True)
        .sample(frac=1, random_state=random_state)
        .reset_index(drop=True)
    )
