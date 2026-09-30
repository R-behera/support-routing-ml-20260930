"""Dependency-free JSON HTTP service for local and container demos."""

from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from support_routing_ml.pipeline import Pipeline


PIPELINE = Pipeline.from_file(
    os.environ.get("MODEL_PATH", "artifacts/model.json")
)


class Handler(BaseHTTPRequestHandler):
    def respond(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self.respond(200, {"status": "ok", "project": PIPELINE.model["project"]})
            return
        self.respond(404, {"error": "not_found"})

    def do_POST(self) -> None:
        if self.path != "/predict":
            self.respond(404, {"error": "not_found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            text = str(payload["text"]).strip()
            if not text:
                raise ValueError("text is required")
            self.respond(200, PIPELINE.run(text))
        except (ValueError, KeyError, json.JSONDecodeError) as error:
            self.respond(400, {"error": str(error)})

    def log_message(self, message: str, *args: object) -> None:
        print(
            json.dumps(
                {
                    "event": "http_request",
                    "client": self.client_address[0],
                    "message": message % args,
                }
            )
        )


def main() -> None:
    port = int(os.environ.get("PORT", "8080"))
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(json.dumps({"event": "service_started", "port": port}))
    server.serve_forever()


if __name__ == "__main__":
    main()
