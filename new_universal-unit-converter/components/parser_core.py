"""Parser core: high-level parse/convert/format functions.

This module depends on the lower-level helpers in `parser_helpers` and
exposes `parse_query`, `convert`, and formatting helpers used by the UI.
"""

from __future__ import annotations

from typing import Any, Dict

from .parser_helpers import normalize_text, tokenize


def format_number(value: float) -> str:
    return f"{value:,.2f}"


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


def _build_velocity_source_unit(first_unit: Dict[str, Any], second_unit: Dict[str, Any]) -> Dict[str, Any] | None:
    if first_unit.get("category") == "length" and second_unit.get("category") == "time":
        return {
            "kind": "UNIT",
            "text": f"{first_unit['text']} per {second_unit['text']}",
            "start": int(first_unit["start"]),
            "end": int(second_unit["end"]),
            "category": "velocity",
            "canonical": f"{first_unit['canonical']} per {second_unit['canonical']}",
            "factor": float(first_unit["factor"]) / float(second_unit["factor"]),
            "alias": f"{first_unit['alias']} per {second_unit['alias']}",
        }
    return None


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
    if source_unit.get("category") != target_unit.get("category") and target_unit.get("category") == "velocity":
        source_candidates = [token for token in tokens if token.get("kind") == "UNIT" and int(token["end"]) <= int(next((token for token in tokens if token.get("kind") == "KEYWORD"), {"start": len(normalized_query)})["start"])]
        if len(source_candidates) >= 2:
            velocity_source = _build_velocity_source_unit(source_candidates[-2], source_candidates[-1])
            if velocity_source is not None:
                source_unit = velocity_source

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


def _format_unit_text(unit: Dict[str, Any]) -> str:
    unit_text = str(unit.get("text", "")).strip()
    if unit.get("category") == "velocity" and " per " not in unit_text and " " in unit_text:
        parts = unit_text.split()
        if len(parts) == 2:
            return f"{parts[0]} per {parts[1]}"
    return unit_text


def format_confirmation(parsed_query: Dict[str, Any]) -> str:
    amount_text = format_number(float(parsed_query["amount"]))
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    category = str(source_unit["category"]).title()
    return (
        f"Understood inquiry **:** `{amount_text} {_format_unit_text(source_unit)} in {_format_unit_text(target_unit)}`  \n"
        f"Detected category **:** `{category}`  \n\n"
        "Submit again or press `Enter` to calculate."
    )


def format_result(parsed_query: Dict[str, Any], result: float) -> str:
    amount_text = format_number(float(parsed_query["amount"]))
    source_unit = parsed_query["source"]
    target_unit = parsed_query["target"]
    return f"Result **:** `{amount_text} {_format_unit_text(source_unit)}` = `{format_number(result)} {_format_unit_text(target_unit)}`"
