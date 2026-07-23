""" Create dashboard layout """

import panel as pn

from components.widgets import (
    text_input, output_area, submit_button,
    logo_pane, github_logo_pane,
)

# --- Info and Links Panes ---

info_pane = pn.pane.Markdown(
    """
    <span style="font-size:36px; color:#C71585; font-family: monospace; font-weight:bold; display:block; padding: 0px 10px 0px 20px;">Universal Unit Converter</span><br>
    <span style="font-size:20px; color:#FDB3FD; font-family: monospace; display:block; padding:0px 10px 0px 20px;">
    Enter a query like `1500 kcal in joules` or `10 miles to km`.<br>
    The first submit shows what the converter understood; submit again or press Enter to calculate.<br>
    If the query cannot be parsed, the app will ask you to rephrase it.<br>
    <br>
    </span>
    """,
)

links_pane = pn.pane.Markdown(
    """
    <span style="font-size:24px; color:#C71585; font-family: monospace; font-weight:bold; padding: 0px 10px 0px 20px;">Visit Project Page on GitHub</span><br>
    <span style="font-size:18px; padding: 0px 10px 0px 20px;">
    [🢅 https://github.com/kuranez/universal-unit-converter](https://github.com/kuranez/universal-unit-converter)
    </span>
    """
)

# --- TOP & UPPER MIDDLE SCREEN: Main Panel (input/output widgets) ---
query_row = pn.Row(
    pn.layout.HSpacer(),
    text_input,                     # Input field
    submit_button,                  # Submit button next to it
    pn.layout.HSpacer(),
    sizing_mode='stretch_width',
)

main_pane = pn.Column(
    pn.layout.VSpacer(),
    query_row,                      # User input (field & button)
    sizing_mode='stretch_both',
)

# --- LOWER MIDDLE SCREEN: Output area with some spacing ---
output_pane = pn.Column(
    output_area,
    pn.layout.VSpacer(),
    sizing_mode='stretch_width',
)

# --- MIDDLE SCREEN: Combine main panel and output with spacing ---
content_panel = pn.Row(
    pn.layout.HSpacer(),
    pn.Column(
        main_pane,
        output_pane,
        sizing_mode='stretch_both',
    ),
    pn.layout.HSpacer(),
    sizing_mode='stretch_both',
)

# --- LOWER SCREEN: Footer with info and logo ---
repo_pane = pn.Row(links_pane, github_logo_pane)

footer_text = pn.Column(
    info_pane,
    repo_pane,
    sizing_mode='stretch_width',
)

footer_row = pn.Row(
    pn.layout.VSpacer(),
    footer_text,
    logo_pane,
    pn.layout.VSpacer(),
    sizing_mode='stretch_width',
)

# --- Final Layout ---
layout = pn.Column(
    content_panel,
    footer_row,
    sizing_mode='stretch_both',
)

def get_dashboard():
    return layout