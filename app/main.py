import uvicorn
from api.app import app
from settings import get_settings


def run():
    settings = get_settings()
    uvicorn.run(
        'main:app',
        host=settings.host,
        port=settings.port,
        workers=settings.workers
    )


if __name__ == "__main__":
    run()
