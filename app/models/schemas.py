from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    role_id: int

    class Config:
        orm_mode = True


class UserRoleBase(BaseModel):
    pass


class UserRoleCreate(UserRoleBase):
    pass


class UserRole(UserRoleBase):
    title: str


class RoleBase(BaseModel):
    title: str


class RoleCreate(RoleBase):
    id: int


class Role(RoleBase):
    id: int
    title: str

    class Config:
        orm_mode = True
