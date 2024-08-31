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
down_revision: Union[str, None] = 'ff1a4a3733a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    task_table = op.create_table(
        'tasks',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('summary', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('status', sa.Enum(TaskMode), nullable=False, default=TaskMode.NEW),
        sa.Column('priority', sa.SmallInteger, default=0),
        sa.Column('owner_id', sa.UUID, nullable=False),
    )
    op.create_foreign_key('fk_task_user', 'tasks', 'users', ['owner_id'], ['id'])

    # Data seed for first task
    op.bulk_insert(task_table, [
        {
            "id": "95955fb1-983f-42fa-97b1-dbb5d78a6ccb",
            "summary": "Do nothing", 
            "description": "Do nothing",
            "status": TaskMode.NEW,
            "priority": 0,
            "owner_id": "07f73797-42f2-4cfa-a658-21a11d93a76d",
        }
    ])

def downgrade() -> None:
    op.drop_table('tasks')
    op.execute("DROP TYPE TaskMode;")