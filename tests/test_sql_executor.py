import pytest
from ironclad.executors.run_sql import ReadOnlySQLExecutor

@pytest.fixture
def executor():
    return ReadOnlySQLExecutor(db_url="sqlite:///:memory:")

def test_write_query_blocked(executor):
    with pytest.raises(ValueError):
        executor.execute({"query": "DELETE FROM users"})
