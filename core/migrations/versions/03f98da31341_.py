"""empty message

Revision ID: 03f98da31341
Revises: 
Create Date: 2018-06-05 11:24:16.249306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f98da31341'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###


def downgrade():
    op.create_table('cities',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('uf', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cities_pkey')
    )
    # ### end Alembic commands ###