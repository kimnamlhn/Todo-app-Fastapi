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
down_revision: Union[str, None] = '1a0af04bfd73'
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
        sa.Column("updated_at", sa.DateTime),
        sa.Column("company_id", sa.UUID, nullable=True)
    )
    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    
    # Add foreign key
    op.create_foreign_key("fk_user_company", "users", "company", ["company_id"],['id'])

    # Data seed for first user
    op.bulk_insert(user_table, [
        {
            "id": "07f73797-42f2-4cfa-a658-21a11d93a76d",
            "email": "fastapi_example@sample.com", 
            "username": "fa_admin",
            "password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
            "company_id": "80668578-146c-413c-aaec-6e8282322bdf",
        }
    ])


def downgrade() -> None:
    op.drop_table("users")
