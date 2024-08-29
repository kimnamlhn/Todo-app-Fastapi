"""create_company_table

Revision ID: 1a0af04bfd73
Revises: 
Create Date: 2024-08-29 15:51:28.654573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a0af04bfd73'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'company',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('company_name', sa.String, nullable=False),
        sa.Column('address', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )

def downgrade() -> None:
    op.drop_table('company')