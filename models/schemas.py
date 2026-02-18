from pydantic import BaseModel
from typing import List, Optional, Any


class ChatRequest(BaseModel):
    model_provider: str
    message: str
    model: str
    

class StandardResponse(BaseModel):
    status: Literal["success", "error"]
    data: Optional[Any] = None
    message: Optional[str] = None
