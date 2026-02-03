from datetime import datetime, timezone

class AuditLogger:
    def log(self, message: str):
        ts = datetime.now(timezone.utc).isoformat()
        print(f"[{ts}] {message}")
