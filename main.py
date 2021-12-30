from fastapi import Depends, FastAPI
from config.settings import Settings, get_settings
from config.database import engine
from database import models

app = FastAPI()


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "env": settings.APP_ENV,
        "mysql_database": settings.MYSQL_DATABASE
    }

models.Base.metadata.create_all(engine)
