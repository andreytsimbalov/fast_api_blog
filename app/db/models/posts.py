from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.models.base import Base, id_type, created_at_type, updated_at_type, is_active_type


class PostType(Enum):
    text = 'text'
    msg = 'message'


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[id_type]
    # Можно сделать "ForeignKey(Users.id)", но могут быть ошибки с циклическим импортом
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    text: Mapped[str]
    type: Mapped[PostType] = mapped_column(default=PostType.msg)
    is_active: Mapped[is_active_type]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[updated_at_type]
