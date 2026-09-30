# Portfolio and Career Mapping

## Project Pitch

**Applied ML Support Router** solves this real-world problem:

Support operations need reproducible routing models that expose confidence and defer uncertain cases.

It combines `text-classification`, `zero-shot-classification`, `sentence-similarity`, `summarization` with data ingestion, evaluation, observability, and scalable
service design.

## Why This Is More Than an API Wrapper

- Owns ingestion, validation, model artifacts, and evaluation datasets.
- Exposes evidence and confidence instead of returning opaque text.
- Includes offline evaluation and a CI release gate.
- Defines tracing, rollback, human review, and failure recovery.
- Provides a realistic path from free local baseline to production stack.

## AI Engineering Job Description Mapping

- Applied NLP classification and confidence calibration
- Human feedback loops and active learning
- Model registry, drift monitoring, and retraining
- Feature, label, and evaluation pipeline design
- Business-aware automation and escalation metrics

## Resume-Ready Impact Targets

Replace targets with measured results after completing the roadmap:

- Reach macro F1 >= 0.85 on a reviewed support set
- Automate >= 60% of tickets at >= 0.90 precision
- Route low-confidence cases to human review
- Detect label and feature drift before SLA impact

Example resume format:

> Built Applied ML Support Router, a production-oriented applied-machine-learning system
> using FastAPI for prediction and feedback endpoints, scikit-learn or LightGBM for production baselines, Sentence Transformers for semantic fallback; measured
> classification_accuracy, automation_coverage, escalation_precision and
> enforced regression thresholds in CI.

## Interview Discussion Areas

- Why this architecture fits the problem and where it fails
- Retrieval/model choice and baseline comparisons
- Evaluation-set construction and metric trade-offs
- Data privacy, authorization, and human escalation
- Scaling, caching, index tuning, and failure recovery
- Model, prompt, dataset, and deployment lineage
