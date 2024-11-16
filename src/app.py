from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from litestar import Litestar
from tortoise import Tortoise

from src.config import TORTOISE_CONFIG
from src.routes import routes


@asynccontextmanager
async def lifespan(app: Litestar) -> AsyncGenerator[None, None]:
    await Tortoise.init(config=TORTOISE_CONFIG)
    yield
    await Tortoise.close_connections()


app = Litestar(
    route_handlers=routes,
    lifespan=[lifespan],
)


if __name__ == '__main__':
    uvicorn.run('src.app:app', host='0.0.0.0', port=8000, reload=True)
