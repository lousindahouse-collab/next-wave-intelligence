from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Next Wave V1.3 API"
    app_env: str = "development"
    database_url: str = "sqlite:///./nextwave.db"
    model_version: str = "NW-1.0"

    # V1.1/V1.2 live discovery
    live_hn_max_items: int = 200
    live_candidate_limit: int = 25
    live_gdelt_validation_limit: int = 8
    live_enable_gdelt: bool = True
    live_http_timeout_seconds: float = 8.0

    # V1.3 Reddit Problem Intelligence. Reddit-approved OAuth access is required.
    reddit_enabled: bool = False
    reddit_client_id: str = ""
    reddit_client_secret: str = ""
    reddit_access_token: str = ""
    reddit_refresh_token: str = ""
    reddit_user_agent: str = "windows:nextwave-local:v1.3 (by /u/YOUR_REDDIT_USERNAME)"
    reddit_search_limit: int = 25
    reddit_max_queries: int = 8
    reddit_time_filter: str = "week"
    reddit_raw_ttl_hours: int = 24
    reddit_http_timeout_seconds: float = 20.0

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
