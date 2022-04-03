from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API made with FastAPI and MongoDB",
    description="This API allows you to interact with a Mongo Data Based through the CRUD functiones detailed below",
    version="1.0"
)

app.include_router(user)

