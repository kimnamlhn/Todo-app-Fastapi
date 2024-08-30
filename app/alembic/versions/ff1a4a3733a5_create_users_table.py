"""create_users_table

Revision ID: ff1a4a3733a5
Revises: 1a0af04bfd73
Create Date: 2024-08-29 15:51:32.531007

"""
from datetime import datetime, timezone
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa

from schemas.user import get_password_hash
from settings import ADMIN_DEFAULT_PASSWORD


# revision identifiers, used by Alembic.
revision: str = 'ff1a4a3733a5'
down_revision: Union[str, None] = 'c4f2ae1d2d1d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # User Table
    user_table = op.create_table(
        "users",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("email", sa.String, unique=True, nullable=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )
    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    # Update Tasks Table
    op.add_column("tasks", sa.Column("owner_id", sa.UUID, nullable=True))
    op.create_foreign_key("fk_task_owner", "tasks", "users", ["owner_id"],['id'])

    # Data seed for first user
    op.bulk_insert(user_table, [
        {
            "id": uuid4(),
            "email": "fastapi_tour@sample.com", 
            "username": "fa_admin",
            "password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        }
    ])


def downgrade() -> None:
    # Rollback foreign key
    op.drop_column("tasks", "owner_id")
    # Rollback foreign key
    op.drop_table("users")
