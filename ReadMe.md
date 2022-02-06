# NanoGUI-stub

- Attention) This library is not completed.
  - I'm not familiar with pybind11-stubgen so that the generated library might be incomplete.
- This package enables showing TypeHint in [NanoGUI for Python](https://github.com/mitsuba-renderer/nanogui).

## What is NanoGUI?

- NanoGUI is GUI library base OpenGL(WebGL?) for C++/Python, which enables to export WebAssembly.

## Generated below procedure

1. Install packages
  - `pip install -U nanogui pybind11-stubs`
2. Generating stubs for NanoGUI
  - `PYTHONPATH=. pybind11-stubgen nanogui --no-setup-py --root-module-suffix="" --ignore-invalid=all --output-dir="./nanogui-stubs"`
3. Fixed a little.
4. Added ReadMe.md and setup.py

## How to install
```bash
pip install -e git+https://github.com/HirotsuguMINOWA/NanoGUI-stub#egg=nanogui-stubs
```
