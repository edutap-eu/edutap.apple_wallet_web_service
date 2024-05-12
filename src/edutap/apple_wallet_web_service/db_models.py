from datetime import datetime
from edutap.wallet_apple import Pass
from edutap.wallet_apple import PassInformation
from pydantic import ConfigDict
from sqlmodel import Field
from sqlmodel import LargeBinary
from sqlmodel import SQLModel


# Based on: https://developer.apple.com/documentation/walletpasses/adding_a_web_service_to_update_passes#3733252


class AppleDeviceRegistry(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    id: int | None = Field(default=None, primary_key=True)
    deviceLibraryIdentitfier: str
    pushToken: str


class ApplePassData(SQLModel, table=True):  # type: ignore[call-arg]
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="allow")

    passTypeIdentifier: str = Field(primary_key=True)
    serialNumber: str = Field(primary_key=True)
    lastUpdateTag: datetime
    passObj: Pass
    passData: PassInformation
    passFiles: list[LargeBinary]


class ApplePassRegistry(SQLModel, table=True):  # type: ignore[call-arg]
    """ """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="allow")

    id: int | None = Field(default=None, primary_key=True)
    deviceLibraryIdentitfier: str
    passTypeIdentifier: str
    serialNumber: str
