import sys
from pathlib import Path

# conftest.py está en: DUAD/python_intermedio/unit_test/
DUAD_DIR = Path(__file__).resolve().parents[2]          # -> DUAD
PY_INTERMEDIO_DIR = DUAD_DIR / "python_intermedio"     # -> DUAD/python_intermedio
PYTHON_BASICO_DIR = DUAD_DIR / "Python"                # -> DUAD/Python

sys.path.insert(0, str(PY_INTERMEDIO_DIR))
sys.path.insert(0, str(PYTHON_BASICO_DIR))