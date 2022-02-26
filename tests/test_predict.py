import pytest
from app import app as current_app


@pytest.fixture()
def app():
    app = current_app
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_snapshot_predict(client, snapshot):
    response = client.post(
        "/predict",
        json={
            "age": {"0": 0.038076},
            "sex": {"0": 0.050680},
            "bmi": {"0": 0.061696},
            "bp": {"0": 0.021872},
            "s1": {"0": -0.044223},
            "s2": {"0": -0.034821},
            "s3": {"0": -0.043401},
            "s4": {"0": -0.002592},
            "s5": {"0": 0.019908},
            "s6": {"0": -0.017646},
        },
    )
    assert response.status_code == 200
    assert "prediction" in response.json
    snapshot.assert_match(response.json)
