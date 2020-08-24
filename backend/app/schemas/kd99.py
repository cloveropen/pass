from typing import Optional
from pydantic import BaseModel, EmailStr

'''字段说明
    主键  id_kd99 number(28,0) not null primary key
    医院编码 HSP_Code varchar2(20) not null 
    操作员编码 opcode varchar2(6) not null
    姓名  opname varchar2(50)
    所属部门(科室) dept_code varchar2(6)
    一级密码 dkd903 varchar2(512) 3DES加密
    二级密码 dkd904 varchar2(512) 3DES加密
    职务 post varchar2(6) 专业技术职务代码（GB8561-2001）  
    是否锁定 is_lock varchar2(1) 0 锁定
    邮箱 email text
    手机号码 tel text
	本人照片 img text base54编码，不大于2M
'''


class Kd99Base(BaseModel):
    hsp_code: str = None
    opcode: str = None
    opname: str = None
    dept_code: Optional[str] = None
    post: Optional[str] = None
    is_lock: str = '0'
    email: Optional[EmailStr] = None
    tel: Optional[str] = None
    img: Optional[str] = None


class Kd99InDBBase(Kd99Base):
    seq_kd99: Optional[int] = None


# Additional properties to return via API
class Kd99(Kd99InDBBase):
    pass


# Additional properties stored in DB
class Kd99InDB(Kd99InDBBase):
    dkd903: str = None
    dkd904: Optional[str] = None
