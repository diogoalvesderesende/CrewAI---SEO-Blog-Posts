# sitecustomize.py
"""
Runs before any other import, even on Streamlit Cloud.
Replaces the old system sqlite3 module with the modern one that ships
inside the pysqlite3-binary wheel (SQLite ≥ 3.45).
"""
import sys

import pysqlite3          # wheel already in requirements.txt
sys.modules["sqlite3"] = pysqlite3
