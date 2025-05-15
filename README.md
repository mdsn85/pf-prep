# pf-prep

# run mypy for type
# mypy src/ --strict

# test APP:
PYTHONPATH=. pytest -q

أنشئ البيئة وشغّلها:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run mypy for type
# mypy src/ --strict

python -m cProfile -o profile_day2.txt path/to/your_script.py
