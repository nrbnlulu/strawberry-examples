"""Add nullable=False

Revision ID: 3a98bc1018d1
Revises: 3320c3c008d2
Create Date: 2021-09-10 15:58:23.998900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a98bc1018d1'
down_revision = '3320c3c008d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('directors', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('movies', 'imdb_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('movies', 'year',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('movies', 'image_url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('movies', 'imdb_rating',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.alter_column('movies', 'imdb_rating_count',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('movies', 'director_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'director_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('movies', 'imdb_rating_count',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('movies', 'imdb_rating',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('movies', 'image_url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('movies', 'year',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('movies', 'imdb_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('directors', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
