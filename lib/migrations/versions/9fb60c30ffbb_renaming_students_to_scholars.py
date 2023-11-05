"""Renaming students to scholars

Revision ID: 9fb60c30ffbb
Revises: 791279dd0760
Create Date: 2023-11-05 09:56:57.029503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fb60c30ffbb'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')