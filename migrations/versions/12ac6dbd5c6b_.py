"""
Migration add table image

Revision ID: 12ac6dbd5c6b
Revises: e8fe75fea167
Create Date: 2021-12-31 07:47:22.852281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12ac6dbd5c6b'
down_revision = 'e8fe75fea167'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('image',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.Text(length=100000), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_charset='utf8mb4',
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_engine='InnoDB'
    )


def downgrade():
    pass
