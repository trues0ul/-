import os
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    assert url, "BASE_URL is not set."
    return url.rstrip("/")

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s
