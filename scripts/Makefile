
PY_VERSION ?= 3.12.3

all: .venv run

.venv:
	uv venv --prompt scripts -p $(PY_VERSION)
	uv pip install -r requirements.txt

run: listagem popula

listagem: listagem.py
	uv run python listagem.py

popula: popula.py
	uv run python popula.py