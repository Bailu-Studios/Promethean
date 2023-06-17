import uvicorn
from fastapi import FastAPI


class HTTPServer:
    app: FastAPI

    def __init__(self, host, port):
        self.app = FastAPI()
        uvicorn.run(
            self.app,
            host=host,
            port=port,
            log_config={
                "version": 1,
                "disable_existing_loggers": False,
                "handlers": {
                    "default": {
                        "class": "promethean.log.LoguruHandler",
                    },
                },
                "loggers": {
                    "uvicorn.error": {"handlers": ["default"], "level": "INFO"},
                    "uvicorn.access": {
                        "handlers": ["default"],
                        "level": "INFO",
                    },
                }
            }
        )
        ...
