from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
from app.core.config import OLLAMA_MODEL, OLLAMA_BASE_URL

load_dotenv()

# 환경변수에서 모델명과 베이스 URL을 가져오기
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")  # 기본 포트

def get_ollama_llm():
    return Ollama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL
    )