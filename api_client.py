import os
import requests

class ApiClient:
    def __init__(self, base_url: str | None = None, session: requests.Session | None = None):
        self.base_url = (base_url or os.getenv("BASE_URL") or "").rstrip("/")
        assert self.base_url, "BASE_URL is not set."
        self.s = session or requests.Session()
        self.s.headers.update({"Content-Type": "application/json"})

    def create_order(self, payload: dict):
        return self.s.post(f"{self.base_url}/api/v1/orders", json=payload, timeout=15)

    def get_order_by_track(self, track: int):
        return self.s.get(f"{self.base_url}/api/v1/orders/track", params={"t": track}, timeout=15)
