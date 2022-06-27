"""empty message

Revision ID: a0313acf5a5f
Revises: 134af4b18185
Create Date: 2022-06-26 21:42:41.548346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0313acf5a5f'
down_revision = '134af4b18185'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('movie_renter_detail_mrtd_mvd_id_fkey', 'movie_renter_detail', type_='foreignkey')
    op.drop_constraint('movie_renter_detail_mrtd_mrth_id_fkey', 'movie_renter_detail', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('movie_renter_detail_mrtd_mrth_id_fkey', 'movie_renter_detail', 'movie_renter_head', ['mrtd_mrth_id'], ['mrth_id'])
    op.create_foreign_key('movie_renter_detail_mrtd_mvd_id_fkey', 'movie_renter_detail', 'ms_movie_dvds', ['mrtd_mvd_id'], ['mvd_id'])
    # ### end Alembic commands ###