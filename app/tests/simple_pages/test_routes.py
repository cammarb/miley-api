def test_index_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200
