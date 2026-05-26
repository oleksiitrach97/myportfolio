"""Root wrapper to launch the Python backend from the repository root.

Use:
  python -m api.server

This wrapper adds the backend/python package root to sys.path and then starts
uvicorn using the backend FastAPI app.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BACKEND_PYTHON = REPO_ROOT / "backend" / "python"
BACKEND_API_SERVER = BACKEND_PYTHON / "api" / "server.py"

if str(BACKEND_PYTHON) not in sys.path:
    sys.path.insert(0, str(BACKEND_PYTHON))

if not BACKEND_API_SERVER.exists():
    raise FileNotFoundError(
        f"Could not find backend API server at {BACKEND_API_SERVER}"
    )

spec = importlib.util.spec_from_file_location("backend_api_server", BACKEND_API_SERVER)
backend = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(backend)

app = backend.app
settings = getattr(backend, "settings", None)

if __name__ == "__main__":
    import uvicorn

    if settings is None:
        raise RuntimeError("Failed to load backend settings from backend API server")

    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.PYTHON_API_PORT,
        reload=False,
    )
