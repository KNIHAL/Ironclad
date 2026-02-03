import re
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

FORBIDDEN = re.compile(
    r"\b(insert|update|delete|drop|alter|truncate|create|replace)\b",
    re.IGNORECASE,
)

class ReadOnlySQLExecutor:
    def __init__(self, db_url: str, timeout_sec: int = 5, max_len: int = 5000):
        self.engine = create_engine(
            db_url,
            execution_options={"statement_timeout": timeout_sec * 1000},
        )
        self.max_len = max_len

    def execute(self, params: dict):
        query = params.get("query", "")

        if not query.strip():
            raise ValueError("Empty query")

        if len(query) > self.max_len:
            raise ValueError("Query too long")

        if FORBIDDEN.search(query):
            raise ValueError("Write operations are not allowed")

        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                rows = [dict(row) for row in result.mappings()]
                return {"rows": rows, "row_count": len(rows)}
        except SQLAlchemyError as e:
            raise RuntimeError(f"SQL error: {e}")
