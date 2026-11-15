"""
Humanize report.json.
"""

from __future__ import annotations

import json
from pathlib import Path


def _normalize_report(report_path: Path) -> None:
    """
    Humanize the report file for pytest-json-report plugin.
    """
    with open(report_path, encoding='utf-8') as fin:
        raw_report = json.load(fin)

    with open(report_path, "w", encoding='utf-8') as f:
        json.dump(raw_report, f, indent=4, ensure_ascii=False)
    return None


if __name__ == "__main__":
    rep_path = Path(__file__).parent / "report.json"
    _normalize_report(rep_path)
