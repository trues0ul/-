def test_get_order_by_track_returns_200(api, created_track):
    resp = api.get_order_by_track(created_track)
    assert resp.status_code == 200
