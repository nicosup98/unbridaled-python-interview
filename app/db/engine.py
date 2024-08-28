from sqlmodel import create_engine
import os
from dotenv import load_dotenv
from sqlmodel import Session


def createEngine():
   load_dotenv()

   dbUrl = os.getenv('DATABASE_URL')
   print(f"db: {dbUrl}")

   return create_engine(dbUrl,echo=True)

def createSession():
   engine = createEngine()
   with Session(engine) as session:
      try:
         yield session
      finally:
         session.close()