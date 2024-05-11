from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class AppleWalletWebServiceSettings(BaseSettings):
    """ """

    model_config = SettingsConfigDict(
        env_prefix="edutap_wallet_apple_wallet_web_service_",
        case_sensitive=False,
        extra="ignore",
    )

    db_host: str | None = None
    db_port: int = 5432
    db_name: str | None = None

    db_username: str | None = None
    db_password: str | None = None
