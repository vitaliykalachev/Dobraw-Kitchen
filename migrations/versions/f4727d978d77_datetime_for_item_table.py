"""datetime for Item table

Revision ID: f4727d978d77
Revises: 7d4a5cae9e40
Create Date: 2023-01-12 11:44:08.034315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4727d978d77'
down_revision = '7d4a5cae9e40'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("items", sa.Column('date_posted', sa.DateTime(), default=sa.func.now()))
    pass


def downgrade() -> None:
    op.drop_column('items', 'date_posted')
    pass
