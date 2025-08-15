import pytest

@pytest.mark.parametrize("payload", [
    {
        "firstName": "Morty",
        "lastName": "Smith",
        "address": "Earth C-137",
        "metroStation": "Citadel",
        "phone": "+10000000001",
        "rentTime": 24,
        "deliveryDate": "2025-08-15T10:00:00Z",
        "color": ["BLACK"],
        "comment": "API autotest"
    }
])
def test_create_and_get_order_by_track(base_url, session, payload):
    print("BASE_URL =", base_url)

    create_url = f"{base_url}/api/v1/orders"
    resp_create = session.post(create_url, json=payload)
    assert resp_create.status_code in (200, 201), \
        f"Create failed: {resp_create.status_code} {resp_create.text}"

    body = resp_create.json()
    assert "track" in body, f"No 'track' in response: {body}"
    track = body["track"]

    get_url = f"{base_url}/api/v1/orders/track"
    resp_get = session.get(get_url, params={"t": track})
    assert resp_get.status_code == 200, \
        f"Get by track failed: {resp_get.status_code} {resp_get.text}"