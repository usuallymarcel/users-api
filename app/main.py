from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users
from app.routes.internal import token

app = FastAPI()

app.include_router(users.router)
app.include_router(token.router)

origins = [
    'http://localhost:8000',
    'http://localhost:5173',
    'https://typings.marcel.co.nz'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)