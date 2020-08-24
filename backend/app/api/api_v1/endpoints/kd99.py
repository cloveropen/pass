from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException

from app.schemas import Kd99
from app.db import Kd99repository
from loguru import logger

router = APIRouter()


@router.get("/", response_model=List[Kd99])
async def read_kd99s() -> list:
    logger.info('获取用户信息---')
    kd99rep = Kd99repository.Kd99rep()
    tresult_lst = await kd99rep.get_kd99_all()
    # 把返回的字符串转换为list
    logger.info('获取用户信息完成')
    return tresult_lst


@router.get("/{opcode}", response_model=Kd99)
async def read_kd99(topcode: str) -> Kd99:
    logger.info('获取' + topcode + '用户信息---')
    kd99rep = Kd99repository.Kd99rep()
    tkd99 = await kd99rep.get_kd99_by_opcode(topcode)
    logger.info('获取' + topcode + '用户信息完成---')
    return tkd99
