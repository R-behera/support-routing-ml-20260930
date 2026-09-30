---
license: mit
library_name: custom
pipeline_tag: text-classification
datasets:
- {{HF_NAMESPACE}}/support-routing-ml-20260930-dataset
tags:
- synthetic-data
- transparent-baseline
- applied-machine-learning
- text-classification
- zero-shot-classification
- sentence-similarity
- summarization
metrics:
- accuracy
---

# Applied ML Support Router Baseline Model

## Model Description

This repository contains a small, transparent prototype model for
**Support operations need reproducible routing models that expose confidence and defer uncertain cases.**

The model combines per-label token weights with IDF-weighted evidence
retrieval. It was generated for reproducible architecture demonstrations and
does not call a hosted LLM.

## Evaluation

- Held-out synthetic examples: 4
- Accuracy: 1
- Intended metrics: classification_accuracy, automation_coverage, escalation_precision

## Intended Use

- Architecture prototyping
- CI and evaluation examples
- Local baseline comparisons
- Educational experimentation

## Hugging Face Task Coverage

- `text-classification`
- `zero-shot-classification`
- `sentence-similarity`
- `summarization`

## Limitations and Risks

Synthetic tickets do not represent every user population or language. Production training data needs consent and bias analysis.

The dataset is synthetic and small. Do not use this model for consequential
decisions without representative data, expert review, and production-grade
evaluation.

## Reproducibility

The linked GitHub repository includes `train.py`, the exact dataset split,
evaluation code, and the model JSON format.
