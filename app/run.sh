#!/usr/bin/env bash
# Launch the Quant Education Streamlit app.
# Uses the pyenv "aa_research" env which already has streamlit + matplotlib + numpy.
set -euo pipefail
cd "$(dirname "$0")"
PY="$HOME/.pyenv/versions/3.12.0/envs/aa_research/bin/streamlit"
if [ ! -x "$PY" ]; then
  PY="$(command -v streamlit)"
fi
exec "$PY" run app.py "$@"
