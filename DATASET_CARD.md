---
license: cc-by-4.0
language:
- en
pretty_name: Applied ML Support Router Synthetic Evaluation Set
size_categories:
- n<1K
task_categories:
- text-classification
tags:
- synthetic
- applied-machine-learning
- evaluation
- text-classification
- zero-shot-classification
- sentence-similarity
- summarization
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: test
    path: data/test.jsonl
---

# Applied ML Support Router Synthetic Dataset

## Summary

This dataset contains 14 training examples and 4
held-out examples for **Support operations need reproducible routing models that expose confidence and defer uncertain cases.**

Every record is synthetic and includes:

- `input`: query, event, or feature description
- `label`: expected class, route, relation, or evidence category
- `context`: synthetic supporting context
- `source`: fictional source identifier
- `variant`: generation pattern
- `synthetic`: always `true`

## Uses

- Reproducible unit and integration tests
- Baseline model training
- Evaluation harness development
- Schema and architecture demonstrations

## Limitations

Synthetic tickets do not represent every user population or language. Production training data needs consent and bias analysis.

This dataset does not represent real users, patients, customers, production
traffic, or licensed media. It must not be presented as real-world evidence.

## Related Model

[{{HF_NAMESPACE}}/support-routing-ml-20260930-model](https://huggingface.co/{{HF_NAMESPACE}}/support-routing-ml-20260930-model)
