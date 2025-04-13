from fastapi import APIRouter
from app.models.schema import RecommendationRequest, RecommendationResponse
from app.llm.ollama_client import get_ollama_llm

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
async def recommend(req: RecommendationRequest):
    llm = get_ollama_llm()
    prompt = f"'{req.user_input}' 성향을 가진 사람에게 수원의 여행지 3곳을 추천해줘."
    result = llm.invoke(prompt)
    recommendations = [line.strip("-• ").strip() for line in result.split("\n") if line.strip()]
    return {"recommendations": recommendations[:3]}