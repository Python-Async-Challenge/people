""" Places microservice. """

import os

import uvicorn
from fastapi import FastAPI

from src.routers import people as router

BASE_ROUTE = '/people'
VERSION_1_BASE_ROUTE = f'{BASE_ROUTE}/v1'

app = FastAPI(  # pylint: disable=invalid-name
    title="People Microservice",
    openapi_url=f"{BASE_ROUTE}/openapi.json",
    docs_url=f"{BASE_ROUTE}/docs",
    redoc_url=None,
    description="People microservice",
    version=os.environ.get('VERSION', '0.0.0')
)

app.include_router(
    router.router,
    prefix=f'{VERSION_1_BASE_ROUTE}/people', tags=['people']
)


@app.get(f'{VERSION_1_BASE_ROUTE}/health-check', tags=['health-check'])
async def health_check():
    """Health Check endpoint."""
    return {'status': 'Ok'}

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                log_level='info', loop='uvloop', reload=True)
