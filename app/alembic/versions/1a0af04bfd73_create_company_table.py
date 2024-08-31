"""create_company_table

Revision ID: 1a0af04bfd73
Revises: 
Create Date: 2024-08-29 15:51:28.654573

"""
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a0af04bfd73'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    company_table = op.create_table(
        'company',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('mode', sa.String, nullable=False),
        sa.Column('rating', sa.SmallInteger, default=0),
    )

    # Data seed for first company
    op.bulk_insert(company_table, [
        {
            "id": "80668578-146c-413c-aaec-6e8282322bdf",
            "name": "Nashtech", 
            "description": "Nashtech vietnam",
            "mode": "active",
            "rating": 5
        }
    ])
    
    
def downgrade() -> None:
    op.drop_table('company')