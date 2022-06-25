"""empty message

Revision ID: 0048ef31b598
Revises: 50853c252ad9
Create Date: 2022-06-25 11:34:45.454845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0048ef31b598'
down_revision = '50853c252ad9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_rental_detail',
    sa.Column('mrtd_mvd_id', sa.Integer(), nullable=False),
    sa.Column('mrtd_mrth_id', sa.Integer(), nullable=False),
    sa.Column('mrtd_create_date', sa.Date(), nullable=True),
    sa.Column('mrtd_create_user', sa.String(length=30), nullable=True),
    sa.Column('mrtd_update_date', sa.Date(), nullable=True),
    sa.Column('mrtd_update_user', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('mrtd_mvd_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_rental_detail')
    # ### end Alembic commands ###
