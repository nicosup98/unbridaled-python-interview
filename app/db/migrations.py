from sqlmodel import SQLModel

from app.db.engine import createEngine
from app.models.Product import Product
from app.models.Variant import Variant


def migration():

   engine = createEngine()

   SQLModel.metadata.create_all(engine)
   

   


if __name__ == "__main__":
   migration()