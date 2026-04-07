"""Add matching_content_reject column to environments table

Revision ID: 003
Revises: 002
Create Date: 2026-04-06

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("environments") as batch_op:
        batch_op.add_column(sa.Column("matching_content_reject", sa.Text(), nullable=True))


def downgrade():
    with op.batch_alter_table("environments") as batch_op:
        batch_op.drop_column("matching_content_reject")
