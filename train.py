"""Rebuild the transparent prototype model from JSONL training data."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


def tokenize(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", value.lower())


def read_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def train(records: list[dict], base_model: dict) -> dict:
    prototypes: dict[str, Counter] = defaultdict(Counter)
    documents_by_id = {}
    for record in records:
        prototypes[record["label"]].update(
            tokenize(f'{record["input"]} {record["context"]}')
        )
        documents_by_id[record["source"]] = {
            "id": record["source"],
            "label": record["label"],
            "text": record["context"],
            "metadata": {
                "synthetic": True,
                "domain": base_model["domain"],
            },
        }

    documents = list(documents_by_id.values())
    document_frequency = Counter()
    for document in documents:
        document_frequency.update(set(tokenize(document["text"])))
    idf = {
        token: round(math.log((len(documents) + 1) / (frequency + 1)) + 1, 6)
        for token, frequency in document_frequency.items()
    }

    return {
        **base_model,
        "prototypes": {
            label: dict(weights) for label, weights in prototypes.items()
        },
        "documents": documents,
        "idf": idf,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", default="data/train.jsonl")
    parser.add_argument("--base-model", default="artifacts/model.json")
    parser.add_argument("--output", default="artifacts/model.json")
    args = parser.parse_args()

    base_model = json.loads(Path(args.base_model).read_text(encoding="utf-8"))
    model = train(read_jsonl(Path(args.train)), base_model)
    Path(args.output).write_text(
        json.dumps(model, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
