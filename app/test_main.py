from fastapi.testclient import TestClient
from sqlmodel import Session

from app.db.engine import createEngine
from .main import createProduct, app
import pytest

@pytest.fixture(name="session")
def session_fixture():
   engine = createEngine()
   with Session(engine) as session:
      yield session
      
@pytest.fixture(name="client")
def client_fixture(session: Session):
   # def get_session_override():
   #       return session
      
   # app.dependency_overrides[get_session] = get_session_override
   client = TestClient(app)
   yield client
   # app.dependency_overrides.clear()
      
def test_create_prodduct(client: TestClient):
   product = { 
            "name": "Standard-hilt lightsaber 4",
            "uom": "pcs",
            "category_name": "sword",
            "is_producible": True,
            "is_purchasable": False,
            "type": "object",
            "purchase_uom": "pcs",
            "purchase_uom_conversion_rate": 1.22,
            "batch_tracked": False,
            "variants": [
               {
                     "sku": "ME",
                     "sales_price": 1300,
                     "purchase_price": 1000,
                     "type": "product",
                     "config_attributes": [
                        {
                           "config_name": "Type",
                           "config_value": "Standard"
                        }
                     ]
               }
            ],
            "additional_info": "additional infoooo"
      }
   response = client.post("/v1/products/create", json=product)
   app.dependency_overrides.clear()
   data = response.json()
   print(f"data: {data}")
   assert response.status_code == 200
   assert data["name"] == "Standard-hilt lightsaber 4"
   assert data["id"] is not None
   assert len(data["variants"]) == 1