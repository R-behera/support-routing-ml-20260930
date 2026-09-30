"""Transparent baseline pipeline for the generated AI project."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path


def tokenize(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", value.lower())


class Pipeline:
    def __init__(self, model: dict):
        self.model = model

    @classmethod
    def from_file(cls, path: str | Path) -> "Pipeline":
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def classify(self, text: str) -> tuple[str, float]:
        tokens = tokenize(text)
        scores = {
            label: sum(weights.get(token, 0) for token in tokens)
            for label, weights in self.model["prototypes"].items()
        }
        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        label, best = ranked[0]
        total = sum(max(score, 0) for _, score in ranked) or 1
        return label, best / total

    def search(self, query: str, limit: int = 3) -> list[dict]:
        query_tokens = set(tokenize(query))
        ranked = []
        for document in self.model["documents"]:
            document_tokens = set(tokenize(document["text"]))
            lexical = sum(
                self.model["idf"].get(token, 1.0)
                for token in query_tokens & document_tokens
            )
            ranked.append({**document, "score": round(lexical, 6)})
        return sorted(ranked, key=lambda item: (-item["score"], item["id"]))[:limit]

    def graph_evidence(self, text: str) -> list[dict]:
        tokens = set(tokenize(text))
        matches = []
        for subject, relation, target in self.model.get("graph_edges", []):
            edge_tokens = set(tokenize(f"{subject} {relation} {target}"))
            overlap = len(tokens & edge_tokens)
            if overlap:
                matches.append(
                    {
                        "subject": subject,
                        "relation": relation,
                        "target": target,
                        "overlap": overlap,
                    }
                )
        return sorted(matches, key=lambda item: -item["overlap"])

    def run(self, text: str) -> dict:
        label, confidence = self.classify(text)
        evidence = self.search(text)
        result = {
            "prediction": label,
            "confidence": round(confidence, 4),
            "requires_review": confidence < self.model["confidence_threshold"],
            "evidence": evidence,
        }
        if self.model["mode"] == "graph":
            result["graph_evidence"] = self.graph_evidence(text)
        if self.model["mode"] == "agent":
            result["proposed_tool"] = label
            result["approval_required"] = label in {
                "request-approval",
                "request-human-help",
            }
        return result
