import sqlite3

class SecurityLogger:
    def __init__(self, db_path="data/sprawl_audit.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        with open("data/schema.sql", "r") as f:
            conn.executescript(f.read())
        conn.close()

    def log_event(self, scene_id, user_choice, is_correct, threat_type):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO audit_logs (scene_id, user_choice, is_correct, threat_type)
            VALUES (?, ?, ?, ?)
        """, (scene_id, user_choice, 1 if is_correct else 0, threat_type))
        conn.commit()
        conn.close()
