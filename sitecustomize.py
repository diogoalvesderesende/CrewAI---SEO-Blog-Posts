import sys

# 1. Load the wheel that carries SQLite ≥ 3.35
import pysqlite3

# 2. Force every future "import sqlite3" to use that wheel
sys.modules["sqlite3"] = pysqlite3 