from fastapi import APIRouter

from src.api.dependencies import USER_AUTH
from src.modules.inh_accounts_sdk import UserTokenData


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_me(user: USER_AUTH) -> UserTokenData:
    return user

