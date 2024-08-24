from models.product import Product
from sqlmodel import Session

def createProduct(session: Session ):
   session.close()