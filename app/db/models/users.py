from datetime import datetime
from sqlalchemy import MetaData, Table, Column, String, Integer, TIMESTAMP, Boolean

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(40), unique=True, index=True),
    Column("name", String(100)),
    Column("hashed_password", String()),
    Column("is_active", Boolean(), default=True, nullable=False),
    Column("create_datetime", TIMESTAMP, default=datetime.utcnow),
    Column("update_datetime", TIMESTAMP, default=datetime.utcnow),
)
