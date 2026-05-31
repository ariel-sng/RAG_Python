from fastapi import FastAPI

from models.chat_request import ChatRequest

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "¡Hola mundo!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "busqueda": q}

@app.post("/chat")
def chatear(request: ChatRequest):
    return {"respuesta": f"Recibí tu mensaje: {request.prompt}"}
