def test_healthcheck(client):
    """
    Check that app is working.
    """
    res = client.get('/healthcheck')
    assert res.status_code == 200
