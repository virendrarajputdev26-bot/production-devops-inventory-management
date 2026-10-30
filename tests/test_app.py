from app.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_add_product():
    client = app.test_client()

    response = client.post(
        "/products",
        json={
            "id": 2,
            "name": "Keyboard",
            "quantity": 5,
            "price": 1000
        }
    )

    assert response.status_code == 201

def test_get_products():
    client = app.test_client()

    response = client.get("/products")

    assert response.status_code == 200
