from fastapi import APIRouter

from .endpoints import *


main_router = APIRouter()

main_router.include_router(user_router)
main_router.include_router(purchase_router)
main_router.include_router(services_router)
# main_router.include_router(wallet_router)
