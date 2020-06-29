
from fastapi.testclient import TestClient
from main import app, VERSION_1_BASE_ROUTE


client = TestClient(app)


def test_health_check():
    response = client.get(f'{VERSION_1_BASE_ROUTE}/health-check')
    assert response.status_code == 200
    assert response.json() == {'status': 'Ok'}
