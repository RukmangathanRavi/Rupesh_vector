from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DATABASE_URL:str
    COHERE:str
    CLAUDE:str
    OPENAI_API_KEY:str
    LANGSMITH:str
    GROQ:str
    HUGGING_FACE:str
    

settings = Settings()