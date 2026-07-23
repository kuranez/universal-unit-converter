# Universal Unit Converter

**Version: 4.0** 

Babby's first GUI project. Unit converter for distances, masses, volumes and energies with minimal UI.

**Supports:**

- Lenght: meter, kilometer, centimeter, inch, mile
- Mass: gram, kilogram, pound
- Volume: liter, milliliter, gallon
- Energy: joule, calorie, kilowatt hour

See the full list of supported canonical units and aliases in [universal-unit-converter/config.py](universal-unit-converter/config.py).

**Features:**
- Minimal vaporwave themed GUI using HoloViz Panel (https://panel.holoviz.org/).
- Updated to text-based input using language parsing.
- Support for many units sourced from NIST SI guidelines.
- WebApp thoroughly tested in many browsers (Chrome, Firefox, Vivaldi)

**Python Dependencies:**

- `panel`

**Launch App:**
- Use the following command in the terminal to launch a local instance of the app in your browser:

```bash
panel serve app.py
```

## 🌐 Web App

> [![Live Demo](https://img.shields.io/badge/🟢%20Live%20App-%20Universal--Unit--Converter-C71585?style=for-the-badge)](https://apps.kuracodez.space/universal-unit-converter/app)
>
> **Try the app - convert units in your browser, just type what you want to convert!.**

---
## Changes

**Version: 4.0**

**What's New (universal-unit-converter vs. older length-unit-converter versions):**

- **New module layout:** the core app and parser live under `universal-unit-converter/` (e.g. `app.py`, `config.py`, `parser_core.py`, `parser_helpers.py`, `widgets.py`, `layout/dashboard.py`).
- **Natural-language parsing:** free-text, text-based input parsing replaced simple dropdown-only conversions.
- **Centralized unit definitions:** all canonical units and aliases are defined in `universal-unit-converter/config.py` for easier maintenance and extension.
- **Broader unit coverage:** additional units (volume, energy, mass) and many aliases added — see `config.py` for the full list.
- **Cleaner asset & component separation:** UI assets and reusable components moved into `assets/` and `components/` respectively.
- **Testing and debug helpers:** a `test_and_debug/` tree with focused tests and debug scripts was added.
- **Legacy preserved:** previous notebooks and simple GUI scripts remain in `old/` and `scripts/` for reference and compatibility.

---
## Screenshot

| v. 4.0 : Minimal Vaporwave themed Web UI                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Screenshot.png\|429](https://raw.githubusercontent.com/kuranez/length-unit-converter/refs/heads/main/screenshots/screenshot_version_4.png) |


---

## Version History

| **Early Panel WebApp (v. 3.0 - v.3.2)**<br>                                                                                         | **Vaporvawe Notebook (v. 2.0)**                                                                                                                                    | **Basic GUI (v. 1.0 - v. 1.4)**                                                                       |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| v. 3.2 [↗](https://raw.githubusercontent.com/kuranez/length-unit-converter/refs/heads/main/screenshots/screenshot_version_3-2.png)              | v. 2.0 [↗](https://raw.githubusercontent.com/kuranez/length-unit-converter/refs/heads/main/screenshots/screenshot_version_2.png)) | v. 1.4 [↗](https://github.com/kuranez/Length-Unit-Converter/tree/unit-converter-basic)                |
| - Widgets: `panel`<br>- Language: English<br>- Vaporwave theme<br>- Improved Layout<br>- Working WebApp! | - Widgets: `ipywidgets`<br>- Language: English<br>-  Cleaned up user interface<br>- Vaporwave themed<br>- ! Theme broken !                                | - Widgets: `ipywidgets`<br>- Language: English<br>- Basic GUI / Notebook<br>- Incl. Conversion Tables |


---

## Coding Learn Progress

I started the project in the beginning of 2024.

**Total Line of Codes:** 1059 \
**Beginning:** 02/2024 \
**Ending:** 03/2025 

| Learning Curve                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Screenshot.png\|429](https://raw.githubusercontent.com/kuranez/Length-Unit-Converter/refs/heads/main/learning-progress/learning%20progress.png) |

### First scripts in Jupyter Notebook

| v. 0.a                                                                                                                                   | v. 0.b                                                                                                                       | v. 0.c                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| v-0a_console-version.py [↗](https://github.com/kuranez/Length-Unit-Converter/blob/main/scripts/v-0a_console-version.py) | v-0b_basic-gui.py [↗](https://github.com/kuranez/Length-Unit-Converter/blob/unit-converter-panel-3-0/scripts/v-0b_basic-gui.py) | v-0c_styled-gui.py [↗](https://github.com/kuranez/Length-Unit-Converter/blob/unit-converter-panel-3-0/scripts/v-0c_styled-gui.py) |
| Simple unit converter script, completely text-based.                                                                                     | Adding GUI elements using `ipywidgets`.                                                                                      | Simple Styling & Layout.                                                                                                       |

---
## Sources

- **JupyterLab**:  Interactive Python Notebooks [↗](https://jupyter.org/)
- **Holoviz Panel**: Data Exploration & Web App Framework [↗](https://panel.holoviz.org/)
- **NIST Guide to the SI**, Appendix B.8: Factors for Units Listed Alphabetically [↗](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8)
