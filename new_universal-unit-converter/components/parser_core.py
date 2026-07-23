"""Parser core: high-level parse/convert/format functions.

This module depends on the lower-level helpers in `parser_helpers` and
exposes `parse_query`, `convert`, and formatting helpers used by the UI.
"""

from __future__ import annotations

from typing import Any, Dict

from .parser_helpers import normalize_text, tokenize


def format_number(value: float) -> str:
    formatted = f"{value:,.12f}".rstrip("0").rstrip(".")
    return formatted or "0"


def _select_units(tokens: list[Dict[str, Any]]) -> tuple[Dict[str, Any], Dict[str, Any]] | None:
    unit_tokens = [token for token in tokens if token.get("kind") == "UNIT"]
    if len(unit_tokens) < 2:
        return None

    keyword_token = next((token for token in tokens if token.get("kind") == "KEYWORD"), None)
    if keyword_token is not None:
        source_candidates = [token for token in unit_tokens if int(token["end"]) <= int(keyword_token["start"])]
        target_candidates = [token for token in unit_tokens if int(token["start"]) >= int(keyword_token["end"])]
        if source_candidates and target_candidates:
            return source_candidates[-1], target_candidates[0]

    return unit_tokens[0], unit_tokens[1]


def parse_query(query: str) -> Dict[str, Any] | None:
    normalized_query = normalize_text(query)
    if not normalized_query:
        return None

    tokens = tokenize(normalized_query)
    if not tokens:
        return None

    amount_token = next((token for token in tokens if token.get("kind") == "NUMBER"), None)
    if amount_token is None:
        return None

    selected_units = _select_units(tokens)
    if selected_units is None:
        return None

    source_unit, target_unit = selected_units
    if source_unit.get("category") != target_unit.get("category"):
        return None

    amount_text = str(amount_token.get("text", ""))
    if not amount_text:
        return None

    amount_position = normalized_query.find(amount_text)
    if amount_position == -1 or amount_position > int(source_unit["start"]):
        return None

    if int(source_unit["start"]) > int(target_unit["start"]):
        return None

    return {
        "amount": float(amount_token["value"]),
        "source": source_unit,
        "target": target_unit,
    }


def convert(parsed_query: Dict[str, Any]) -> float:
    amount = float(parsed_query["amount"])
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    return amount * float(source_unit["factor"]) / float(target_unit["factor"])


def format_confirmation(parsed_query: Dict[str, Any]) -> str:
    amount_text = format_number(float(parsed_query["amount"]))
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    category = str(source_unit["category"]).title()
    return (
        f"Understood inquiry **:** `{amount_text} {source_unit['text']} in {target_unit['text']}`  \n"
        f"Detected category **:** `{category}`  \n\n"
        "Submit again or press `Enter` to calculate."
    )


def format_result(parsed_query: Dict[str, Any], result: float) -> str:
    amount_text = format_number(float(parsed_query["amount"]))
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    return f"Result **:** `{amount_text} {source_unit['text']}` = `{format_number(result)} {target_unit['text']}`"
