# Applied ML Support Router

A transparent text-classification baseline for routing support requests with confidence and escalation.

Generated on 2026-09-30 as an independent production-AI architecture project.

## Real-World Problem

Support operations need reproducible routing models that expose confidence and defer uncertain cases.

## Hugging Face Tasks

- `text-classification`
- `zero-shot-classification`
- `sentence-similarity`
- `summarization`

## Recommended Production Stack

- FastAPI for prediction and feedback endpoints
- scikit-learn or LightGBM for production baselines
- Sentence Transformers for semantic fallback
- MLflow for experiments and model registry
- PostgreSQL for labels and human feedback
- Evidently-style drift and quality monitoring

## Included

- Runnable Python pipeline with no runtime dependencies
- Local JSON HTTP inference service
- Public-data API connector with explicit provenance
- Reproducible training script
- Held-out evaluation command
- Synthetic dataset with explicit provenance
- Trained transparent baseline model
- Architecture and production-boundary documentation
- Unit tests, CI workflow, and Dockerfile
- Hugging Face-ready model and dataset cards

## Architecture

1. Synthetic labeled dataset
1. Prototype text classifier
1. Confidence threshold
1. Human escalation queue
1. Accuracy and coverage report

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full flow and production
boundaries.

## Quick Start

```bash
python3 -m unittest discover -s tests
PYTHONPATH=src python3 -m support_routing_ml.cli "I was charged twice for the same subscription"
PYTHONPATH=src python3 evaluate.py
PYTHONPATH=src python3 -m support_routing_ml.service
```

The service exposes `GET /health` and `POST /predict`.

Rebuild the model:

```bash
python3 train.py
```

## Baseline Evaluation

- Held-out synthetic examples: 4
- Accuracy: 1
- Target metrics: classification_accuracy, automation_coverage, escalation_precision

This score verifies that the code and evaluation contract work. It does not
claim production performance.

## Hugging Face Artifacts

When the controller has a Hugging Face token and namespace configured, it
publishes:

- Dataset: `support-routing-ml-20260930-dataset`
- Model: `support-routing-ml-20260930-model`

## Portfolio Value

This repository maps to production AI engineering work in:

- Applied NLP classification and confidence calibration
- Human feedback loops and active learning
- Model registry, drift monitoring, and retraining
- Feature, label, and evaluation pipeline design
- Business-aware automation and escalation metrics

See [PORTFOLIO.md](PORTFOLIO.md) for resume-ready impact targets and interview
discussion areas.

## 1-3 Month Expansion

Follow [ROADMAP.md](ROADMAP.md) to add real-world APIs, a stronger open model,
durable orchestration, evaluation, observability, scalability testing, and a
public deployment.

## Safety

Synthetic tickets do not represent every user population or language. Production training data needs consent and bias analysis.

Review [ARCHITECTURE.md](ARCHITECTURE.md),
[PRODUCTION.md](PRODUCTION.md), [SECURITY.md](SECURITY.md),
[MODEL_CARD.md](MODEL_CARD.md), and [DATASET_CARD.md](DATASET_CARD.md) before
adapting this project.
