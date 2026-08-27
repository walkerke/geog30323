#!/bin/bash
# Launch the Baby Names Explorer (from this directory)
cd "$(dirname "$0")"
uv run --with streamlit --with pandas --with pyarrow --with plotly streamlit run app.py
