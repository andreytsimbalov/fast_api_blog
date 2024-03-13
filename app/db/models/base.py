from datetime import datetime
from typing import Annotated

from sqlalchemy import func, String
from sqlalchemy.orm import DeclarativeBase, mapped_column


id_type = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
is_active_type = Annotated[bool, mapped_column(default=True)]
# Можно сделать "server_default=text("TIMEZONE('utc', now())")" для приведения времени к UTC
created_at_type = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at_type = Annotated[
    datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)
]

str_50 = Annotated[str, 50]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_50: String(50)
    }
