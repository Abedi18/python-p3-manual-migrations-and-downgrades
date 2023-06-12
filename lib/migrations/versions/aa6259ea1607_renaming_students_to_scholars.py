"""Renaming students to scholars

Revision ID: aa6259ea1607
Revises: 791279dd0760
Create Date: 2023-06-12 09:34:47.798688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa6259ea1607'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
