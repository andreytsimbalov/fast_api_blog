import uvicorn
from api.app import app
from config import settings


def run():
    uvicorn.run(
        'main:app',
        host=settings.host,
        port=settings.port,
        workers=settings.workers
    )


if __name__ == "__main__":
    run()
