import sqlite3
from datetime import datetime
from typing import Any, Dict, Optional

class SharedMemory:
    def __init__(self, db_path: str = 'shared_memory.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source TEXT,
                    type TEXT,
                    timestamp TEXT,
                    extracted_values TEXT,
                    thread_id TEXT
                )
            ''')

    def log(self, source: str, type_: str, extracted_values: str, thread_id: Optional[str] = None):
        with self.conn:
            self.conn.execute(
                'INSERT INTO memory (source, type, timestamp, extracted_values, thread_id) VALUES (?, ?, ?, ?, ?)',
                (source, type_, datetime.utcnow().isoformat(), extracted_values, thread_id)
            )

    def get_last(self) -> Optional[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM memory ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'source': row[1],
                'type': row[2],
                'timestamp': row[3],
                'extracted_values': row[4],
                'thread_id': row[5]
            }
        return None
