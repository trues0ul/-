import os
import json
from pathlib import Path
import pytest
from src.api_client import ApiClient

# (опционально) поддержка .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

ROOT = Path(__file__).resolve().parent

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    assert url, "BASE_URL is not set. Put it in .env or set env var."
    return url.rstrip("/")

@pytest.fixture(scope="session")
def api(base_url):
    return ApiClient(base_url)

@pytest.fixture(scope="session")
def orders_data():
    with open(ROOT / "testdata" / "orders.json", "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def any_order_payload(orders_data):
    return orders_data[0]

@pytest.fixture
def created_track(api, any_order_payload) -> int:
    resp = api.create_order(any_order_payload)
    assert resp.status_code in (200, 201), f"Create failed: {resp.status_code} {resp.text}"
    payload = resp.json()
    assert "track" in payload, f"No track in response: {payload}"
    track = payload["track"]
    assert isinstance(track, int)
    return track
