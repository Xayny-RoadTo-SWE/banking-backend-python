import os 

# ==========================================
# Configurações do Banco de Dados
# ==========================================

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5433"))
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "batatinha123")
DB_NAME = os.getenv("DB_NAME", "sunfire_bank")

# ==========================================
# Configurações de Segurança e Autenticação (JWT)
# ==========================================

SECRET_KEY = os.getenv("SECRET_KEY", "chave_secreta_super_segura_sunfire_bank")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKE_EXPIRE_MINUTES", "30"))
class Settings:
    # URL de conexão montada dinamicamente
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Expondo as variáveis de segurança para o resto do sistema
    SECRET_KEY: str = SECRET_KEY
    ALGORITHM: str = ALGORITHM
    ACCESS_TOKE_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES

settings = Settings()

