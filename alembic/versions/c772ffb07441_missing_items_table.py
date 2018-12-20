"""missing-items-table

Revision ID: c772ffb07441
Revises: 1486dc6d0b6b
Create Date: 2019-01-11 15:49:38.635915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c772ffb07441'
down_revision = '1486dc6d0b6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('missing_items',
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('response_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['resources.id'], ),
    sa.ForeignKeyConstraint(['response_id'], ['responses.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('missing_items')
    # ### end Alembic commands ###
