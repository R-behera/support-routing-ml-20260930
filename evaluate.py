"""Evaluate the generated baseline on the held-out synthetic split."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from support_routing_ml.pipeline import Pipeline


def read_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="artifacts/model.json")
    parser.add_argument("--test", default="data/test.jsonl")
    args = parser.parse_args()

    pipeline = Pipeline.from_file(args.model)
    records = read_jsonl(Path(args.test))
    correct = sum(
        pipeline.run(f'{record["input"]} {record["context"]}')["prediction"]
        == record["label"]
        for record in records
    )
    accuracy = correct / max(len(records), 1)
    report = {
        "examples": len(records),
        "accuracy": round(accuracy, 4),
        "synthetic_evaluation": True,
    }
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if accuracy >= 0.5 else 1)


if __name__ == "__main__":
    main()
