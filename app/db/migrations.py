from sqlmodel import SQLModel
from dotenv import load_dotenv
from .engine import createEngine


def migration():

   engine = createEngine()

   SQLModel.metadata.create_all(engine)
   
if __name__ == '__main__':
   migration()
