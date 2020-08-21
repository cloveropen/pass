from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import PROJECT_NAME,API_V1_STR,ALLOWED_HOSTS
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
#from app.core.events import create_start_app_handler, create_stop_app_handler

from loguru import logger

app = FastAPI(
    title=PROJECT_NAME, openapi_url=f"{API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.add_event_handler("startup", create_start_app_handler(app))
#app.add_event_handler("shutdown", create_stop_app_handler(app))

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
logger.info("启动完成,开始导入路由")
app.include_router(api_router, prefix=API_V1_STR)