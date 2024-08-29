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
   client = TestClient(app)
   yield client
      
def test_create_prodduct(client: TestClient):
   product = {
      "name": "Standard-hilt lightsaber",
      "uom": "pcs",
      "category_name": "lightsaber",
      "is_producible": True,
      "is_purchasable": True,
      "type": "product",
      "purchase_uom": "pcs",
      "purchase_uom_conversion_rate": 1,
      "batch_tracked": False,
      "variants": [
         {
               "sku": "EM",
               "sales_price": 40,
               "product_id": 1,
               "purchase_price": 0,
               "type": "product",
               "config_attributes": [
                  {
                     "config_name": "Type",
                     "config_value": "Standard"
                  }
               ]
         }
      ],
      "additional_info": "additional info",
   }
   response = client.post("/v1/products/create", json=product)
   data = response.json()
   print(f"data: {data}")
   assert response.status_code == 200
   assert data["name"] == "Standard-hilt lightsaber"
   assert data["id"] is not None
   assert len(data["variants"]) == 1
   assert data["variants"][0]["id"]
   assert data["id"] == data["variants"][0]["product_id"]
   
def test_create_bad_product(client: TestClient):
   product = { 
            "uom": "pcs",
            "category_name": 33,
            "is_producible": True,
            "is_purchasable": False,
            "type": "object",
            "purchase_uom": "pcs",
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
            "additional_info": 100
      }
   
   response = client.post("/v1/products/create", json=product)
   data = response.json()
   print(f"data: {data}")
   assert response.status_code != 200

def test_create_product_duplicated_variant(client: TestClient):
   product = { 
            "name": "Standard-hilt lightsaber 44",
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
                     "sku": "MA",
                     "sales_price": 1300,
                     "purchase_price": 1000,
                     "type": "product",
                     "config_attributes": [
                        {
                           "config_name": "Type",
                           "config_value": "Standard"
                        }
                     ]
               },
               {
                     "sku": "MA",
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
   data = response.json()
   print(f"data: {data}")
   assert response.status_code != 200