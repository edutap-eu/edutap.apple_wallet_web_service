from fastapi import APIRouter
from fastapi import Request

# from fastapi.logger import logger
from fastapi.responses import Response
from fastapi.security import HTTPBearer
from pydantic import ConfigDict


router = APIRouter(prefix="/apple_update_service/v1")



@router.post("/devices/{device_id}/registrations/{pass_type_id}/{serial_number}")
async def register_pass(
    device_id: str, pass_type_id: str, serial_number: str, data, request: Request
):
    """ """

    print(f"register pass: {device_id=}, {pass_type_id=}, {serial_number=}, {data=}, {request=}")

    breakpoint()
    return Response(status_code=201)

    return Response(status_code=304)

    return Response(status_code=401)


@router.get("/devices/{device_id}/registrations/{pass_type_id}")
async def update_pass(
    device_id: str, pass_type_id: str, passesUpdatedSince: str, request: Request
):
    """ """
    print(f"update pass: {device_id=}, {pass_type_id=}, {passesUpdatedSince=}, {request=}")

    return Response(status_code=200)

    return Response(status_code=204)

    return Response(status_code=401)


@router.delete("/devices/{device_id}/registrations/{pass_type_id}/{serial_number}")
async def unregister_pass(
    device_id: str, pass_type_id: str, serial_number: str, request: Request
):
    """ """
    print(f"unregister pass: {device_id=}, {pass_type_id=}, {serial_number=}, {request=}")

    return Response(status_code=200)

    return Response(status_code=401)


@router.get("/passes/{pass_type_id}/{serial_number}")
async def send_updated_pass(pass_type_id: str, serial_number: str, request: Request):
    """ """
    print(f"send updated pass: {pass_type_id=}, {serial_number=}, {request=}")

    return Response(status_code=200)

    return Response(status_code=401)


@router.post("/log")
async def device_log(data, request: Request):
    """ """
    print(f"log: {data=}, {request=}")

    return Response(status_code=200)
