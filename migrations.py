from sqlmodel import create_engine,SQLModel
from dotenv import load_dotenv
import os

def migration():
   load_dotenv()

   dbUrl = os.getenv('DATABASE_URL')

   engine = create_engine(dbUrl,echo=True)


   SQLModel.metadata.create_all(engine)
   
if __name__ == '__main__':
   migration()
