from datetime import datetime
from datetime import timezone
from edutap.wallet_apple.models import Pass
from sqlmodel import Field
from sqlmodel import SQLModel


# Based on: https://developer.apple.com/documentation/walletpasses/adding_a_web_service_to_update_passes#3733252


class AppleDeviceRegistry(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    id: int | None = Field(default=None, primary_key=True)
    deviceLibraryIdentitfier: str
    pushToken: str


class ApplePassData(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    passTypeIdentifier: str = Field(primary_key=True)
    serialNumber: str = Field(primary_key=True)
    lastUpdateTag: datetime = Field(default_factory=datetime.now(tz=timezone.utc))
    passfile: Pass
    # passObj: Pass
    # passData: PassInformation
    # passFiles: list[LargeBinary]


class ApplePassRegistry(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    id: int | None = Field(default=None, primary_key=True)
    deviceLibraryIdentitfier: str
    passTypeIdentifier: str
    serialNumber: str
