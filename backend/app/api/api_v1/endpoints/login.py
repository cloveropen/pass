from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app import schemas
from app.core import security
from app.db import Kd99repository
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from loguru import logger

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    logger.info("开始进入login_access_token")
    # OAuth2 compatible token login, get an access token for future requests
    kd99rep = Kd99repository.Kd99rep()
    tkd99 = await kd99rep.authenticate(opcode=form_data.username, password=form_data.password)

    if not tkd99:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not kd99rep.is_active(tkd99):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            tkd99["opcode"], expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/login/test-token", response_model=schemas.Kd99)
async def test_token(token :str ) -> Any:
    kd99rep = Kd99repository.Kd99rep()
    logger.info("开始调用et_kd99_by_opcode")
    tkd99 = await kd99rep.get_current_user(token)
    # Test access token
    return tkd99


'''
@router.post("/password-recovery/{email}", response_model=schemas.Msg)
def recover_password(email: str):
    pass
    , db: Session = Depends(deps.get_db)) -> Any:
    """
    Password Recovery
    """
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(
        email_to=user.email, email=email, token=password_reset_token
    )
    return {"msg": "Password recovery email sent"}


@router.post("/reset-password/", response_model=schemas.Msg)
def reset_password():
    pass
    
    token: str = Body(...),
    new_password: str = Body(...),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Reset password
    """
    email = verify_password_reset_token(token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system.",
        )
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    hashed_password = get_password_hash(new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()
    return {"msg": "Password updated successfully"}
'''
