# Trade

API for doing stock trading.

## Setup

1. Within a python virtual environment, run `pip install -r requirements.txt` to install project dependencies.
2. Within project's root directory, create `credentials.py` (git untracked) file then add the following snippet.
```python
import os

os.environ.setdefault('IQ_OPTIONS_API_EMAIL', '<replace-with-your-email>')
os.environ.setdefault('IQ_OPTIONS_API_PASSWORD', '<replace-with-your-password>')
```
## Execution

Run `python trade.py <binary(default)/digital>`