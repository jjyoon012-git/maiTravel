from pydantic import BaseModel
from typing import List

class RecommendationRequest(BaseModel):
    user_input: str

class RecommendationResponse(BaseModel):
    recommendations: List[str]