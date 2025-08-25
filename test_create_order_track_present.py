def test_create_order_returns_track(api, any_order_payload):
    resp = api.create_order(any_order_payload)
    body = resp.json()
    assert "track" in body
    assert isinstance(body["track"], int)
