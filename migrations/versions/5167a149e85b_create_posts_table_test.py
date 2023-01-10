"""create posts table test

Revision ID: 5167a149e85b
Revises: 
Create Date: 2023-01-10 16:44:44.913171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5167a149e85b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
