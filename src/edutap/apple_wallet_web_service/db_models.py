from .config import AppleWalletWebServiceSettings
from datetime import datetime
from datetime import timezone
from sqlalchemy.types import JSON
from sqlmodel import create_engine
from sqlmodel import Field
from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig
from typing import Any
from typing import Generator


# from typing import Literal
# from edutap.wallet_apple.models import Pass


# Based on: https://developer.apple.com/documentation/walletpasses/adding_a_web_service_to_update_passes#3733252


class AppleDeviceRegistry(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    id: int | None = Field(default=None, primary_key=True)
    deviceLibraryIdentitfier: str
    pushToken: str
    registrationTime: datetime = Field(default=datetime.now(tz=timezone.utc))


class ApplePassData(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    model_config = SQLModelConfig(
        arbitrary_types_allowed=True,
    )

    passTypeIdentifier: str = Field(primary_key=True)
    serialNumber: str = Field(primary_key=True)
    lastUpdateTag: datetime = Field(default=datetime.now(tz=timezone.utc))
    # passStatus: Literal["downloaded", "registered", "unregistered"]
    # passfile: JSON
    # passFiles: list[LargeBinary]


class ApplePassRegistry(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    id: int | None = Field(default=None, primary_key=True)
    deviceLibraryIdentitfier: str
    passTypeIdentifier: str
    serialNumber: str
    registrationTime: datetime = Field(default=datetime.now(tz=timezone.utc))


def get_session() -> Generator[Session, Any, Any]:
    print("Read Settings for Create Session")
    settings: AppleWalletWebServiceSettings = AppleWalletWebServiceSettings()
    print(settings)

    print("Create Engine")
    engine = create_engine(
        f"{settings.db.type}+{settings.db.driver}://{settings.db.username}:{settings.db.password}@{settings.db.host}{':' + str(settings.db.port) if settings.db.port != 5432 else ''}/{settings.db.name}",
        echo=True,
    )
    print(engine.url)

    # Generate Tables
    SQLModel.metadata.create_all(engine)
    print("Create Session")
    with Session(engine) as session:
        yield session
