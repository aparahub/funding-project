import json
import os
import runpy
from pathlib import Path

PROJECT_FOLDER = Path('/Users/apara/funding-project')
PYTHON_SCRIPT = PROJECT_FOLDER / 'query_csv.py'
OUTPUT_FILE = Path(__file__).resolve().parents[1] / 'public' / 'answers.json'

# Run query_csv.py from its own folder so relative CSV paths work.
os.chdir(PROJECT_FOLDER)
variables = runpy.run_path(str(PYTHON_SCRIPT))

answers = {}
for i in range(1, 11):
    key = f'answer{i}'
    value = variables.get(key)
    if value is None:
        raise KeyError(f'{key} was not found in query_csv.py')
    answers[key] = str(value)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text(json.dumps(answers, indent=2), encoding='utf-8')
print(f'Answers exported to {OUTPUT_FILE}')
