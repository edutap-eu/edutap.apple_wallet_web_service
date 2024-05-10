from .service import router
from .config import AppleWalletWebServiceSettings
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi import Request
from fastapi.logger import logger
from importlib.metadata import version

import asyncio
import uvicorn


logger.setLevel("DEBUG")

__version__ = version("edutap.apple_wallet_web_service")


settings = AppleWalletWebServiceSettings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initializing
    
    app.include_router(router)

    logger.info("creating stream processor for google wallet notifications")
    # asyncio.create_task(
    #     process_messages(
    #         settings.broker_url,
    #         settings.topic
    #     )
    # )
    yield
    # Shutdown


app = FastAPI(
    title="eduTAP Apple Wallet Web Service",
    description="A fastAPI based Web Service for Apple Wallet",
    # summary=""" """,
    version=__version__,
    lifespan=lifespan,
)


@app.get("/")
async def info():
    return {
        "package": "edutap.apple_wallet_web_service",
        "version": __version__,
        # "broker_url": settings.broker_url,
        # "topic": settings.notification_topic,
    }


@app.get("/openapi.json")
async def openapi():
    return app.openapi()


@app.post("/test/message")
async def test_message(request: Request, msg: str):
    return
    # await kafka_producer.send_and_wait("test", msg.encode("utf-8"))


def main():
    uvicorn.run(
        "edutap.apple_wallet_web_service.standalone:app",
        host="0.0.0.0",
        port=8084,
        log_level="debug",
        reload=True,
    )


if __name__ == "__main__":
    main()
