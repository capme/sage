"""
Migration add table variant

Revision ID: 09480e0e951b
Revises: 12ac6dbd5c6b
Create Date: 2021-12-31 10:45:35.475059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09480e0e951b'
down_revision = '12ac6dbd5c6b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('variant',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=True),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('size', sa.String(length=80), nullable=False),
        sa.Column('color', sa.String(length=80), nullable=False),
        sa.Column('images', sa.Text(length=100000), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['product_id'], ['product.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id'),
        mysql_charset='utf8mb4',
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_engine='InnoDB'
    )


def downgrade():
    op.drop_table('variant')
