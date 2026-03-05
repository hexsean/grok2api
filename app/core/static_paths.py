"""
Static asset path resolver.

Resolve static directory across different deployment layouts
(local source tree, packaged runtime, Vercel function bundle).
"""

from pathlib import Path
from functools import lru_cache
import os


def _unique_paths(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    unique: list[Path] = []
    for path in paths:
        key = str(path.resolve()) if path.exists() else str(path)
        if key in seen:
            continue
        seen.add(key)
        unique.append(path)
    return unique


@lru_cache(maxsize=1)
def find_static_dir() -> Path | None:
    override = os.getenv("STATIC_DIR", "").strip()
    candidates: list[Path] = []
    if override:
        candidates.append(Path(override))

    base_dir = Path(__file__).resolve().parents[2]
    cwd = Path.cwd()
    candidates.extend(
        [
            base_dir / "app" / "static",
            cwd / "app" / "static",
            base_dir / "public" / "static",
            cwd / "public" / "static",
            base_dir / "static",
            cwd / "static",
        ]
    )

    for path in _unique_paths(candidates):
        if path.exists() and path.is_dir():
            return path
    return None

