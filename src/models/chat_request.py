from pydantic import BaseModel, ConfigDict

class ChatRequest(BaseModel):
    prompt: str

    # si incluye algo más que no sea el prompt, se rechaza el request 
    model_config = ConfigDict(extra="forbid")