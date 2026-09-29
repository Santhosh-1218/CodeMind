import pytest
from app.hindsight.client import hindsight_client

@pytest.mark.asyncio
async def test_hindsight_live_connection():
    # Test live recall endpoint with configured bank
    memories = await hindsight_client.recall("SQL injection security rules")
    assert isinstance(memories, list)
