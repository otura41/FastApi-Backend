"""create todos table

Revision ID: 17f2799a5bd3
Revises: 
Create Date: 2025-05-27 10:47:49.920331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17f2799a5bd3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     """Upgrade schema."""
#     pass

def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)


def downgrade():
    op.execute("drop table todos;")