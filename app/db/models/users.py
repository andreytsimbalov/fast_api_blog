from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import Base, id_type, is_active_type, created_at_type, updated_at_type, str_50


class Users(Base):
    __tablename__ = "users"

    id: Mapped[id_type]
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str_50]
    hashed_password: Mapped[str]
    is_active: Mapped[is_active_type]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[updated_at_type]
