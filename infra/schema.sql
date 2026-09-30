CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS artifact_versions (
  id bigserial PRIMARY KEY,
  artifact_type text NOT NULL,
  artifact_name text NOT NULL,
  version text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (artifact_type, artifact_name, version)
);

CREATE TABLE IF NOT EXISTS evaluation_runs (
  id bigserial PRIMARY KEY,
  model_version text NOT NULL,
  dataset_version text NOT NULL,
  metrics jsonb NOT NULL,
  passed boolean NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS documents (
  id text PRIMARY KEY,
  tenant_id text NOT NULL,
  content text NOT NULL,
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
  embedding vector(384)
);

CREATE INDEX IF NOT EXISTS documents_tenant_idx ON documents (tenant_id);
CREATE INDEX IF NOT EXISTS documents_embedding_hnsw_idx
  ON documents USING hnsw (embedding vector_cosine_ops);
