import uvicorn
from fastapi import FastAPI, status, Response
from api.routes import api_version_one
from fastapi.middleware.cors import CORSMiddleware
from api.utils.settings import settings
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Auth",
    description="Auth API",
    version="1.0.0",
)

origins = [
    "http://localhost:3000"
]


app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_version_one)


@app.get("/", tags=["Home"])
async def get_root(request: Request):
    return JSONResponse("Auth API  ")

