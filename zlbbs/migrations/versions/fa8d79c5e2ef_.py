"""empty message

Revision ID: fa8d79c5e2ef
Revises: 2966c20ba224
Create Date: 2019-01-09 17:14:03.079379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa8d79c5e2ef'
down_revision = '2966c20ba224'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('_password', sa.String(length=500), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cms_user')
    op.drop_constraint('cms_role_user_ibfk_2', 'cms_role_user', type_='foreignkey')
    op.create_foreign_key(None, 'cms_role_user', 'cms_users', ['cms_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cms_role_user', type_='foreignkey')
    op.create_foreign_key('cms_role_user_ibfk_2', 'cms_role_user', 'cms_user', ['cms_user_id'], ['id'])
    op.create_table('cms_user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8_bin', length=20), nullable=False),
    sa.Column('_password', mysql.VARCHAR(collation='utf8_bin', length=500), nullable=False),
    sa.Column('email', mysql.VARCHAR(collation='utf8_bin', length=50), nullable=False),
    sa.Column('join_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_bin',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('cms_users')
    # ### end Alembic commands ###
