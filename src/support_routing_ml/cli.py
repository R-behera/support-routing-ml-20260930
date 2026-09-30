"""Command-line interface."""

from __future__ import annotations

import argparse
import json

from support_routing_ml.pipeline import Pipeline


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    parser.add_argument("--model", default="artifacts/model.json")
    args = parser.parse_args()

    result = Pipeline.from_file(args.model).run(args.text)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
