from fastapi import FastAPI

app = FastAPI()

@app.post("/v1/products/create")
def hello():
   return "hello"