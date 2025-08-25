def test_create_order_returns_2xx(api, any_order_payload):
    resp = api.create_order(any_order_payload)
    assert resp.status_code in (200, 201)
