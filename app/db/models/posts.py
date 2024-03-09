from datetime import datetime
from sqlalchemy import MetaData, Table, Column, ForeignKey, Integer, String, TIMESTAMP, Boolean

from app.db.models.users import users

metadata = MetaData()


posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", ForeignKey(users.c.id), nullable=False),
    Column("text", String),
    Column("is_active", Boolean(), default=True, nullable=False),
    Column("create_datetime", TIMESTAMP, default=datetime.utcnow),
    Column("update_datetime", TIMESTAMP, default=datetime.utcnow),
)
