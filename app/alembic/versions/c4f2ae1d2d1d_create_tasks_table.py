"""create_tasks_table

Revision ID: c4f2ae1d2d1d
Revises: ff1a4a3733a5
Create Date: 2024-08-29 15:51:36.917841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from schemas.task import TaskMode


# revision identifiers, used by Alembic.
revision: str = 'c4f2ae1d2d1d'
down_revision: Union[str, None] = '1a0af04bfd73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('status', sa.Enum(TaskMode), nullable=False, default=TaskMode.NEW),
        sa.Column('company_id', sa.UUID, nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )
    op.create_foreign_key('fk_task_company', 'tasks', 'company', ['company_id'], ['id'])

def downgrade() -> None:
    op.drop_table('tasks')
    op.execute("DROP TYPE TaskMode;")