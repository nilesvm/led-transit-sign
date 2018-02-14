"""added index to stop_id

Revision ID: 360a6a3e1d83
Revises: b112caaac731
Create Date: 2018-02-13 15:30:28.167950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '360a6a3e1d83'
down_revision = 'b112caaac731'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_stop_stop_id'), 'stop', ['stop_id'], unique=True)
    op.drop_constraint('stop_stop_id_key', 'stop', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('stop_stop_id_key', 'stop', ['stop_id'])
    op.drop_index(op.f('ix_stop_stop_id'), table_name='stop')
    # ### end Alembic commands ###
