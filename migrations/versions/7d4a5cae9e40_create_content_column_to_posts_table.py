"""create content column to posts table

Revision ID: 7d4a5cae9e40
Revises: 5167a149e85b
Create Date: 2023-01-10 17:13:30.094459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d4a5cae9e40'
down_revision = '5167a149e85b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
