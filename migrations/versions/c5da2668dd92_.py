"""empty message

Revision ID: c5da2668dd92
Revises: 519f92404df5
Create Date: 2022-06-25 11:05:48.548486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5da2668dd92'
down_revision = '519f92404df5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_on_ban',
    sa.Column('uob_id', sa.Integer(), nullable=False),
    sa.Column('uob_msu_id', sa.Integer(), nullable=False),
    sa.Column('uob_desc', sa.String(length=200), nullable=False),
    sa.Column('uob_status', sa.String(length=1), nullable=False),
    sa.Column('uob_banned_date', sa.Date(), nullable=False),
    sa.Column('uob_create_date', sa.Date(), nullable=True),
    sa.Column('uob_create_user', sa.String(length=30), nullable=True),
    sa.Column('uob_update_date', sa.Date(), nullable=True),
    sa.Column('uob_update_user', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('uob_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_on_ban')
    # ### end Alembic commands ###
