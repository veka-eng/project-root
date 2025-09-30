from app.main import create_app

def test_index():
    app = create_app()
    client = app.test_client()
    rv = client.get("/")
    assert rv.status_code == 200
    assert "Hello" in rv.get_json()["message"]
