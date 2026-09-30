# 12-Week Solo Engineering Roadmap

The generated repository is the tested foundation. The plan below is scoped for
one engineer working part time over one to three months.

## Weeks 1-2: Problem and Data Contract

- Define users, decisions, failure severity, and non-goals.
- Integrate one public source: GitHub Issues API.
- Add raw-data snapshots, schema validation, and provenance.
- Build a 50-100 example human-reviewed evaluation set.

## Weeks 3-4: Retrieval or Model Baseline

- Reproduce the included transparent baseline.
- Add one stronger open model for text-classification.
- Compare quality, latency, memory, and operational complexity.
- Establish versioned experiment reports.

## Weeks 5-6: Orchestration and Product API

- Implement typed FastAPI endpoints and asynchronous jobs.
- Add workflow state, retries, idempotency, and human review.
- Persist artifacts and metadata in PostgreSQL.
- Add tenant or role filters before retrieval and actions.

## Weeks 7-8: Evaluation and LLMOps

- Expand adversarial, low-confidence, and failure-mode tests.
- Add model, prompt, dataset, and deployment lineage.
- Instrument traces and metrics with OpenTelemetry.
- Block releases when critical metrics regress.

## Weeks 9-10: Scale and Reliability

- Run load tests against the targets in `PRODUCTION.md`.
- Tune caches, batching, indexes, and concurrency.
- Add rollback, circuit breakers, and degraded-mode behavior.
- Document cost and capacity assumptions.

## Weeks 11-12: Portfolio Release

- Deploy a public demo using only safe sample data.
- Publish architecture decisions and a short technical write-up.
- Record measured impact metrics and limitations.
- Add screenshots, sequence diagrams, and a two-minute demo video.

## Definition of Done

- CI tests, evaluation gates, and security checks pass.
- A reviewer can reproduce training and evaluation.
- Public APIs are used within their terms and rate limits.
- Production claims are backed by measured evidence.
- Model and dataset cards describe limitations honestly.
