from fastapi import Depends, FastAPI
from typing import Annotated

app = FastAPI(
    title='auth API',
    description='An API to test several authentification methods',
    version='0.1.0',
)


@app.get('/')
async def home():
    return {
        'message': 'Welcome to my server!'
    }
