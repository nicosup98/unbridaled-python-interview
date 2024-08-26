from sqlmodel import create_engine
import os

def createEngine():
   load_dotenv()

   dbUrl = os.getenv('DATABASE_URL')

   return create_engine(dbUrl,echo=True)