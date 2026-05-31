from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "¡Hola mundo!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "busqueda": q}