import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # SQL Server Config
    SQLSERVER_HOST: str = os.getenv("SQLSERVER_HOST")
    SQLSERVER_PORT: str = os.getenv("SQLSERVER_PORT", "1433")  # default SQL Server port
    SQLSERVER_DATABASE: str = os.getenv("SQLSERVER_DATABASE")
    SQLSERVER_USER: str = os.getenv("SQLSERVER_USER")
    SQLSERVER_PASSWORD: str = os.getenv("SQLSERVER_PASSWORD")
    SQLSERVER_DRIVER: str = os.getenv(
        "SQLSERVER_DRIVER",
        "ODBC Driver 17 for SQL Server"
    )

    # OpenAI Models
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    CHAT_MODEL: str = os.getenv("CHAT_MODEL", "gpt-4.1")
    LOG_FILE_PATH:str = os.getenv("LOG_FILE_PATH")
    LOG_HEADER:list = os.getenv("LOG_HEADER")
    
    # Semantic Cache Vector Store
    VECTOR_CACHE_PATH: str = os.getenv("VECTOR_CACHE_PATH", "./VECTOR_CACHE_PATH.index")
    METADATA_PKL:str = os.getenv("METADATA_PKL")
    VECTOR_DIMENSION:int = os.getenv("VECTOR_DIMENSION")
    CACHE_SEMATIC_MATCHING:float = float(os.getenv("CACHE_SEMATIC_MATCHING", 0.90))


