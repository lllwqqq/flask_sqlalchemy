"""empty message

Revision ID: 309f7f1957bd
Revises: 410c9f6fe8fa
Create Date: 2018-11-19 16:56:40.182829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '309f7f1957bd'
down_revision = '410c9f6fe8fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('context', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('article')
    # ### end Alembic commands ###