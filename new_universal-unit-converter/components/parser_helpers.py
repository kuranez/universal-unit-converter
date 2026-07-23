"""Parser helper utilities: normalization, tokenization, and low-level finders.

This module builds `UNIT_MATCHERS` from the `UNIT_TABLE` in config.py and
exposes `normalize_text`, `tokenize`, `find_number`, and `find_units` helpers
used by the parser core.
"""

from __future__ import annotations

from typing import Any, Dict, List
import re

from config import UNIT_TABLE as CONFIG_UNIT_TABLE


def normalize_text(text: str) -> str:
    cleaned = text.lower().replace("μ", "u").replace("µ", "u")
    cleaned = cleaned.replace("→", " to ").replace("=", " to ")
    cleaned = re.sub(r"(?<=\d)(?=[a-z])", " ", cleaned)
    cleaned = re.sub(r"(?<=[a-z])(?=\d)", " ", cleaned)
    cleaned = re.sub(r"[^a-z0-9\s\.,\-\+]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


KEYWORD_PATTERN = re.compile(r"\b(?:in|to|into)\b", re.IGNORECASE)
TOKEN_KIND_PRIORITY = {"UNIT": 0, "NUMBER": 1, "KEYWORD": 2}


def _build_word_token(text: str, start: int) -> Dict[str, Any] | None:
    stripped = text.strip()
    if not stripped:
        return None
    offset = text.find(stripped)
    return {
        "kind": "WORD",
        "text": stripped,
        "start": start + offset,
        "end": start + offset + len(stripped),
    }


def _emit_word_tokens(fragment: str, start: int) -> List[Dict[str, Any]]:
    tokens: List[Dict[str, Any]] = []
    cursor = 0
    for part in fragment.split():
        part_start = fragment.find(part, cursor)
        token = _build_word_token(part, start + part_start)
        if token is not None:
            tokens.append(token)
        cursor = part_start + len(part)
    return tokens


UNIT_MATCHERS: List[Dict[str, Any]] = []
for category, units in CONFIG_UNIT_TABLE.items():
    for canonical_name, factor, aliases in units:
        for alias in aliases:
            normalized_alias = normalize_text(alias)
            UNIT_MATCHERS.append(
                {
                    "category": category,
                    "canonical": canonical_name,
                    "factor": factor,
                    "alias": normalized_alias,
                    "pattern": re.compile(rf"(?<!\w){re.escape(normalized_alias)}(?!\w)"),
                }
            )

UNIT_MATCHERS.sort(key=lambda item: len(str(item["alias"])), reverse=True)

NUMBER_PATTERN = re.compile(
    r"(?<!\w)[+-]?(?:\d[\d,]*\.?\d*|\.\d+)(?:e[+-]?\d+)?(?!\w)", re.IGNORECASE
)
CONNECTOR_PATTERN = re.compile(r"\b(?:in|to|into)\b", re.IGNORECASE)


def tokenize(text: str) -> List[Dict[str, Any]]:
    normalized_text = normalize_text(text)
    if not normalized_text:
        return []

    candidates: List[Dict[str, Any]] = []

    for match in NUMBER_PATTERN.finditer(normalized_text):
        amount_text = match.group(0)
        try:
            amount_value = float(amount_text.replace(",", ""))
        except ValueError:
            continue
        candidates.append(
            {
                "kind": "NUMBER",
                "text": amount_text,
                "value": amount_value,
                "start": match.start(),
                "end": match.end(),
            }
        )

    for match in KEYWORD_PATTERN.finditer(normalized_text):
        candidates.append(
            {
                "kind": "KEYWORD",
                "text": match.group(0),
                "start": match.start(),
                "end": match.end(),
            }
        )

    for unit_matcher in UNIT_MATCHERS:
        pattern = unit_matcher["pattern"]
        if not isinstance(pattern, re.Pattern):
            continue
        for match in pattern.finditer(normalized_text):
            candidates.append(
                {
                    "kind": "UNIT",
                    "text": match.group(0),
                    "start": match.start(),
                    "end": match.end(),
                    "category": unit_matcher["category"],
                    "canonical": unit_matcher["canonical"],
                    "factor": unit_matcher["factor"],
                    "alias": unit_matcher["alias"],
                }
            )

    candidates.sort(
        key=lambda item: (
            item["start"],
            -(item["end"] - item["start"]),
            TOKEN_KIND_PRIORITY.get(str(item["kind"]), 99),
        )
    )

    tokens: List[Dict[str, Any]] = []
    cursor = 0
    for candidate in candidates:
        if candidate["start"] < cursor:
            continue

        if cursor < candidate["start"]:
            tokens.extend(_emit_word_tokens(normalized_text[cursor:candidate["start"]], cursor))

        tokens.append(candidate)
        cursor = candidate["end"]

    if cursor < len(normalized_text):
        tokens.extend(_emit_word_tokens(normalized_text[cursor:], cursor))

    return tokens


def find_number(text: str) -> tuple[float, str] | None:
    match = NUMBER_PATTERN.search(text)
    if not match:
        return None

    amount_text = match.group(0).replace(",", "")
    try:
        return float(amount_text), amount_text
    except ValueError:
        return None


def find_units(text: str) -> List[Dict[str, Any]]:
    matches: List[Dict[str, Any]] = []
    for unit_matcher in UNIT_MATCHERS:
        pattern = unit_matcher["pattern"]
        if not isinstance(pattern, re.Pattern):
            continue
        for match in pattern.finditer(text):
            matches.append(
                {
                    "start": match.start(),
                    "end": match.end(),
                    "text": match.group(0),
                    "category": unit_matcher["category"],
                    "canonical": unit_matcher["canonical"],
                    "factor": unit_matcher["factor"],
                    "alias": unit_matcher["alias"],
                }
            )

    matches.sort(key=lambda item: (item["start"], -(item["end"] - item["start"])))
    resolved_matches: List[Dict[str, Any]] = []
    last_end = -1
    for match in matches:
        if match["start"] >= last_end:
            resolved_matches.append(match)
            last_end = match["end"]
    return resolved_matches
