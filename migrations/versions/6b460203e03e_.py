"""empty message

Revision ID: 6b460203e03e
Revises: c976d0499aaf
Create Date: 2020-12-11 17:47:35.278703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b460203e03e'
down_revision = 'c976d0499aaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('settings')
    # ### end Alembic commands ###
