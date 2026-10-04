from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "VoxPlan API"
    database_url: str = "postgresql://user:password@localhost:5432/voice_note_planner"
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = "changeme"
    llm_api_key: str = ""
    speech_to_text_api_key: str = ""
    resend_api_key: str = ""
    resend_from: str = "onboarding@resend.dev"

    class Config:
        env_file = ".env"


settings = Settings()
