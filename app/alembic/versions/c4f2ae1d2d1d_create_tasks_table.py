"""create_tasks_table

Revision ID: c4f2ae1d2d1d
Revises: ff1a4a3733a5
Create Date: 2024-08-29 15:51:36.917841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4f2ae1d2d1d'
down_revision: Union[str, None] = 'ff1a4a3733a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
