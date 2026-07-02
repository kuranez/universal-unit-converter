"""Main application file."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import panel as pn

import components.widgets as widgets
from components.widgets import text_input, output_area, submit_button

from layout.dashboard import get_dashboard
from components.parser_core import (
    parse_query,
    convert,
    format_confirmation,
    format_result,
)
from components.parser_helpers import normalize_text

# --- Load Panel Extensions ---
pn.extension(theme="dark")


# --- Global State ---
pending_query_signature: str | None = None

# --- Functions for Handling User Input ---
def get_current_query() -> str:
    return (text_input.value_input or text_input.value or "").strip()


def submit(event: object | None = None) -> None:
    global pending_query_signature

    query = get_current_query()
    normalized_query = normalize_text(query)
    parsed_query = parse_query(query)

    if parsed_query is None:
        pending_query_signature = None
        output_area.object = "Please rephrase inquiry"
        return

    if pending_query_signature == normalized_query:
        output_area.object = format_result(parsed_query, convert(parsed_query))
        pending_query_signature = None
        text_input.value = ""  # Clear the input field
        return

    pending_query_signature = normalized_query
    output_area.object = format_confirmation(parsed_query)


# --- Button Callbacks ---
submit_button.on_click(submit)
text_input.param.watch(submit, "enter_pressed")
output_area.object = "Enter a query like `1500 kcal in joules` , then submit again or press  `Enter` to calculate. Supported units include `length` , `mass` , `time` , `energy` and more. <br>"

# --- Serve Layout ---
dashboard = get_dashboard()
dashboard.servable()


def main() -> None:
    pn.serve(dashboard, show=True, start=True, title="Universal Unit Converter")


if __name__ == "__main__":
    main()