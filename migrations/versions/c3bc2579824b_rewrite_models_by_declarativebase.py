"""rewrite models by DeclarativeBase

Revision ID: c3bc2579824b
Revises: f6b9572425e1
Create Date: 2024-03-14 00:22:31.961747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c3bc2579824b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('type', postgresql.ENUM('text', 'msg', name='posttype'), autoincrement=False, nullable=False),
        sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='posts_user_id_fkey', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    op.create_table('users',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('email', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
        sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
        sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###