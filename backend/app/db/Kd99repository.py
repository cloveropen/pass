from typing import Optional

import asyncpg
from fastapi.security import OAuth2PasswordBearer

from app.core.config import DATABASE_URL
from app.core.security import verify_password, ALGORITHM
from app.schemas import Kd99
from loguru import logger
from fastapi import Depends, HTTPException, status
from app import schemas
from pydantic import ValidationError
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY,API_V1_STR
from jose import jwt


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{API_V1_STR}/login/access-token"
)

class Kd99rep:
    def __init__(self):
        pass

    # 获取用户列表
    @classmethod
    async def get_kd99_all(cls) -> list:
        # 创建连接数据库的驱动，创建连接的时候要使用await
        conn = await asyncpg.connect(DATABASE_URL)

        # 调用await conn.fetchrow执行select语句，获取满足条件的单条记录
        # 调用await conn.fetch执行select语句，获取满足条件的全部记录
        rows = await conn.fetch("select * from clover_login.kd99")
        # 返回的是一个Record对象，这个Record对象等于将返回的记录进行了一个封装
        tlst = []
        for row in rows:
            tlst.append(dict(row))

        # 关闭连接
        await conn.close()
        return tlst


    # 获取指定用户信息
    @classmethod
    async def get_kd99_by_opcode(cls,opcode: str) -> Kd99:
        # 创建连接数据库的驱动，创建连接的时候要使用await
        conn = await asyncpg.connect(DATABASE_URL)
        tsql = f"SELECT * FROM clover_login.kd99 where opcode='{opcode}'"
        tkd99 = await conn.fetchrow(tsql)
        # 返回的是一个Record对象，这个Record对象等于将返回的记录进行了一个封装

        # 关闭连接
        await conn.close()
        return tkd99

    # 验证用户
    @classmethod
    async def authenticate(cls, opcode: str, password: str) -> Optional[Kd99]:
        logger.info("opcode="+opcode+" passwd="+password)
        #conn = await asyncpg.connect(DATABASE_URL)
        #tsql = "SELECT * FROM clover_login.kd99 where opcode='" + opcode + "'"
        #tkd99 = await conn.fetchrow(tsql)
        ## 关闭连接
        #await conn.close()
        tkd99 = await cls.get_kd99_by_opcode(opcode)

        logger.info("tkd99="+tkd99["opcode"]+" "+tkd99["dkd903"])
        if not tkd99:
            logger.info("查询用户失败")
            return None
        if not verify_password(password, tkd99["dkd903"]):
            logger.info("验证密码失败")
            return None
        return tkd99

    # 用户是否锁定
    async def is_active(self, user: Kd99) -> bool:
        tb: bool = False
        if user.is_lock.strip() == '0':
            tb = True

        return tb

    #####################
    @classmethod
    def get_current_user(cls,token: str = Depends(reusable_oauth2)) -> schemas.Kd99:
        logger.info("开始验证token"+token)
        try:
            payload = jwt.decode(
                token, SECRET_KEY, algorithms=[ALGORITHM]
            )
            logger.info(payload.values())
            token_data = schemas.TokenPayload(**payload)
        except (jwt.JWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )
        logger.info("-------------------------------------")
        logger.info(token_data.json())
        user = cls.get_kd99_by_opcode(token_data.sub)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @classmethod
    def get_current_active_user(cls,current_user: schemas.Kd99 = Depends(get_current_user)) -> schemas.Kd99:
        if not cls.is_active(current_user):
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

    '''
    def get_current_active_superuser(
        current_user: schemas.Kd99 = Depends(get_current_user),
    ) -> schemas.Kd99:
        kd99rep = Kd99repository.Kd99rep()
        if not crud.user.is_superuser(current_user):
            raise HTTPException(
                status_code=400, detail="The user doesn't have enough privileges"
            )
        return current_user
    '''