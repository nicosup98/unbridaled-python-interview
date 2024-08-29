from sqlmodel import SQLModel

from app.db.engine import createEngine
from app.models.Product import Product
from app.models.Variant import Variant


def clearDB():
   engine = createEngine()
   
   SQLModel.metadata.drop_all(engine)
   
def mainDrop():
   print("WARNING".center(30,"-"))
   resp = input("are you sure to drop the db?? s/N: ")
   if resp == "s":
      clearDB()
      
if __name__ == "__main__":
   mainDrop()