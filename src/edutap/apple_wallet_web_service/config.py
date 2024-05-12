from edutap.wallet_apple.settings import AppleWalletSettings
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """ """

    model_config = SettingsConfigDict(
        env_prefix="edutap_wallet_apple_wallet_web_service_db_",
        case_sensitive=False,
        extra="ignore",
    )

    type: str | None = "postgresql"
    driver: str | None = "psycopg2"
    host: str | None = None
    port: int = 5432
    name: str | None = None

    username: str | None = None
    password: str | None = None


class AppleWalletWebServiceSettings(BaseSettings):
    """ """

    model_config = SettingsConfigDict(
        env_prefix="edutap_wallet_apple_wallet_web_service_",
        case_sensitive=False,
        extra="ignore",
    )

    auth_required: bool = True
    log_file: Path

    apple: AppleWalletSettings = AppleWalletSettings()
    db: DatabaseSettings = DatabaseSettings()
