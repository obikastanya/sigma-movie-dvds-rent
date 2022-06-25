"""empty message

Revision ID: c3f495ece122
Revises: c25c5fecbb0d
Create Date: 2022-06-25 12:04:11.549886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3f495ece122'
down_revision = 'c25c5fecbb0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courier',
    sa.Column('msc_id', sa.Integer(), nullable=False),
    sa.Column('msc_desc', sa.Integer(), nullable=False),
    sa.Column('msc_active_status', sa.Integer(), nullable=False),
    sa.Column('ri_create_date', sa.Date(), nullable=True),
    sa.Column('ri_create_user', sa.String(length=30), nullable=True),
    sa.Column('ri_update_date', sa.Date(), nullable=True),
    sa.Column('ri_update_user', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('msc_id')
    )
    op.create_table('movie_returned_detail',
    sa.Column('mrd_id', sa.Integer(), nullable=False),
    sa.Column('mrd_mrh_id', sa.Integer(), nullable=False),
    sa.Column('mrd_mvd_id', sa.Integer(), nullable=False),
    sa.Column('mrd_dvd_desc', sa.Date(), nullable=False),
    sa.Column('mrd_create_date', sa.Date(), nullable=True),
    sa.Column('mrd_create_user', sa.String(length=30), nullable=True),
    sa.Column('mrd_update_date', sa.Date(), nullable=True),
    sa.Column('mrd_update_user', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('mrd_id')
    )
    op.create_table('movie_returned_head',
    sa.Column('mrh_id', sa.Integer(), nullable=False),
    sa.Column('mrh_mrth_id', sa.Integer(), nullable=False),
    sa.Column('mrh_mrth_msu_id', sa.Integer(), nullable=False),
    sa.Column('mrth_return_date', sa.Date(), nullable=False),
    sa.Column('mrh_create_date', sa.Date(), nullable=True),
    sa.Column('mrh_create_user', sa.String(length=30), nullable=True),
    sa.Column('mrh_update_date', sa.Date(), nullable=True),
    sa.Column('mrh_update_user', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('mrh_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_returned_head')
    op.drop_table('movie_returned_detail')
    op.drop_table('courier')
    # ### end Alembic commands ###