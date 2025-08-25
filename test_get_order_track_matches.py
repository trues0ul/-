def test_get_order_by_track_matches_track(api, created_track):
    resp = api.get_order_by_track(created_track)
    data = resp.json()
    # на некоторых стендах объект в поле "order", на других — сразу в корне
    order = data.get("order", data)
    assert order.get("track") == created_track
